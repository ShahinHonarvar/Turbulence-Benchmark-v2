from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[1:9])).lower()
    palindromes = set()
    for length in range(7, 9):
        for perm in permutations(s, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
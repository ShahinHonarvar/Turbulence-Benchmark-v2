from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(5, len(s) + 1):
        for perm in permutations(s, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
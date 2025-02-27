from itertools import permutations

def palindromes_between_indices(s):
    substr = ''.join(filter(str.isalpha, s[2:10].lower()))
    palindromes = set()
    for length in range(4, len(substr) + 1):
        for perm in permutations(substr, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
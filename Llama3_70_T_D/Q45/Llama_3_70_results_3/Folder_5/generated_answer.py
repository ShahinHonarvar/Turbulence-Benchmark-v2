from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(4, len(s) + 1):
        for perm in permutations(s, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
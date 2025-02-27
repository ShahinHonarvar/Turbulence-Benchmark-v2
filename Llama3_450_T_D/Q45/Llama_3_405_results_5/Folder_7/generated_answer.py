import itertools

def palindromes_between_indices(s):
    s = s[1:10].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(7, len(s) + 1):
        for perm in itertools.permutations(s, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
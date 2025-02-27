from itertools import permutations

def palindromes_between_indices(s):
    start, end = (5, 7)
    if len(s) <= end:
        return set()
    substr = ''.join([c.lower() for c in s[start:end + 1] if c.isalpha()])
    palindromes = set()
    for perm in permutations(substr):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 4:
            palindromes.add(perm_str)
    return palindromes
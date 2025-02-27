from itertools import permutations, chain
    import re

def palindromes_between_indices(string):
    if len(string) < 8:
        return set()
    substring = string[:8]
    substring = substring.lower()
    palindromes = set()
    perms = chain.from_iterable((permutations(substring, i + 1) for i in range(len(chars))))
    for perm in perms:
        perm_str = ''.join(perm)
        if re.fullmatch('[a-z]{7,}', perm_str) and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes
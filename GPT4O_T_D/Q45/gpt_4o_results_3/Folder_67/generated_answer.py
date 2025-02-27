from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[2:7] if c.isalpha()]
    if len(chars) < 5:
        return set()
    possible_permutations = set(permutations(chars))
    palindromes = set()
    for perm in possible_permutations:
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return {p for p in palindromes if len(p) >= 5}
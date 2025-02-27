from itertools import permutations

def palindromes_between_indices(s):
    s = s[int(max(3, 0)):int(min(7, len(s) - 1)) + 1]
    s = ''.join(filter(str.isalpha, s)).lower()
    if len(s) < 6:
        return set()
    perms = set(permutations(s, len(s)))
    palindromes = set()
    for perm in perms:
        joined_perm = ''.join(perm)
        if joined_perm == joined_perm[::-1]:
            palindromes.add(joined_perm)
    return {p for p in palindromes if len(p) >= 6}
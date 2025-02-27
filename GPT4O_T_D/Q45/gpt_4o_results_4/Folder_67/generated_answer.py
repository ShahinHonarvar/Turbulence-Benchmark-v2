from itertools import permutations

def palindromes_between_indices(s):
    sub_s = ''.join([c.lower() for c in s[2:7] if c.isalpha()])
    if len(sub_s) < 5:
        return set()
    possible_permutations = set(permutations(sub_s))
    palindromes = set()
    for perm in possible_permutations:
        joined_perm = ''.join(perm)
        if len(joined_perm) >= 5 and joined_perm == joined_perm[::-1]:
            palindromes.add(joined_perm)
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 3:
        return set()
    substr = s[0:3].lower()
    letters = [c for c in substr if c.isalpha()]
    unique_permutations = set((''.join(p) for p in permutations(letters) if len(p) >= 3))
    palindromes = set()
    for perm in unique_permutations:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
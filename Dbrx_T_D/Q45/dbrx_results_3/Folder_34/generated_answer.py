from itertools import permutations

def palindromes_between_indices(s):
    letters = s[5:8].lower()
    perms = [''.join(p) for i in range(1, 5) for p in permutations(letters, i)]
    return {perm + perm[::-1] for perm in perms if len(perm) >= 4}
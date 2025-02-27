from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:3] if char.isalpha())).lower()
    perms = [''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters, i)]
    return set((perm for perm in perms if perm == perm[::-1]))
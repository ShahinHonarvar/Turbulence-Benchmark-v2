from itertools import permutations

def palindromes_between_indices(s):
    valid_chars = list(set(s[4:10].lower()))
    perm = [''.join(p) for i in range(1, 6) for p in permutations(valid_chars, i)]
    return set((x for x in perm if x == x[::-1]))
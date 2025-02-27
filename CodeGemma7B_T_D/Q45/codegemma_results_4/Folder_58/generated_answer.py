from itertools import permutations

def palindromes_between_indices(string):
    return set((f'{''.join(p)}' for p in permutations(string) if ''.join(p[0:7]).lower() == ''.join(p[0:6:-1]).lower()))
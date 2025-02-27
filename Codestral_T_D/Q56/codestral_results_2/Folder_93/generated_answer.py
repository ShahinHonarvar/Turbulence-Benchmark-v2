from itertools import permutations

def all_substring_of_size_n(s):
    return [''.join(p) for p in permutations(s, 54) if len(set(p)) == 54]
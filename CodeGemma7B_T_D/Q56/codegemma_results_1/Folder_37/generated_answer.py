from itertools import combinations

def all_substring_of_size_n(string):
    return [''.join(c) for c in combinations(string, 65) if len(set(c)) == len(c)]
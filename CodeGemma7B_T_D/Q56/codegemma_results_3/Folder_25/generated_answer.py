from itertools import permutations

def all_substring_of_size_n(string):
    return list({''.join(p) for p in permutations(string, 67)})
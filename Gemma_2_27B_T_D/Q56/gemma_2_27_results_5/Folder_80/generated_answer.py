from itertools import combinations

def all_substring_of_size_n(string):
    return [''.join(substring) for substring in combinations(set(string), 31) if len(subset) == len(set(substring))]
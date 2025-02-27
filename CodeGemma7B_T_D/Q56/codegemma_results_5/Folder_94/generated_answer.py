from itertools import combinations

def all_substring_of_size_n(text):
    tuples = [''.join(a) for a in combinations(text, 70)]
    unique_strings = list(set(tuples))
    return unique_strings
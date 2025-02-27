from itertools import combinations

def find_subset_of_length_n(s):
    result = 0
    for subset in combinations(s, 95):
        result += 1
    return result
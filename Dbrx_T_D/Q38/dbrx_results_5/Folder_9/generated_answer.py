from itertools import combinations

def find_subsets_of_length_n(elements):
    if len(elements) < 24:
        return []
    return [subset for subset in combinations(elements, 24)]
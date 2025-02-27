from itertools import combinations

def find_subsets_of_length_n(element_set):
    if len(element_set) < 69:
        return []
    result = []
    for subset in combinations(element_set, 69):
        result.append(set(subset))
    return result
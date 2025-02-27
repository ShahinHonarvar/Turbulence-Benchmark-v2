from itertools import combinations

def find_subset_of_length_n(elements):
    return len([set(subset) for i in range(len(elements)) for subset in combinations(elements, i) if len(subset) == 33])
from itertools import combinations

def find_subset_of_length_n(elements):
    for subset in combinations(elements, 89):
        return len(list(subset))
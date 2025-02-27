from itertools import combinations

def find_subset_of_length_n(elements):
    return len([subset for subset in powerset(elements) if len(subset) == 85])

def powerset(iterable):
    s = list(iterable)
    return [set(combination) for len_set in range(len(s) + 1) for combination in combinations(s, len_set)]
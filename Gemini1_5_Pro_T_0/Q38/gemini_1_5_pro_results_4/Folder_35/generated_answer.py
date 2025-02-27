import itertools

def find_subset_of_length_n(set_of_elements):
    return len(set([subset for subset in powerset(set_of_elements) if len(subset) == 300]))

def powerset(s):
    return set((frozenset(subset) for i in range(len(s) + 1) for subset in itertools.combinations(s, i)))
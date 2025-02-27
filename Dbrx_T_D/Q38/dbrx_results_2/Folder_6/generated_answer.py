def find_subset_of_length_n(elements):
    subsets = [p for p in itertools.permutations(elements, 89)]
    return len(subsets)
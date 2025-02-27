def find_subset_of_length_n(elements):
    subsets = []
    for subset in itertools.combinations(elements, 219):
        subsets.append(subset)
    return len(subsets)
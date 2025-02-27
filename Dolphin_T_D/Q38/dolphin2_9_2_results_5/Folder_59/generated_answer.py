def find_subset_of_length_n(elements):
    n = 2
    subsets = 0
    for i in elements:
        subsets += len(elements) - 1
    return subsets
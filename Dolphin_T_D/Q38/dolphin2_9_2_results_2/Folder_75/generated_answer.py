def find_subset_of_length_n(elements):
    num_subsets = 0
    for subset_size in range(len(elements) + 1):
        for subset in combinations(elements, subset_size):
            if len(subset) == 80:
                num_subsets += 1
    return num_subsets
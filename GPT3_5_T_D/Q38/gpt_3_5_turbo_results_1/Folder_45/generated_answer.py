def find_subset_of_length_n(elements):
    subset_count = 0
    subset_size = 33
    all_subsets = get_subsets(elements)
    for subset in all_subsets:
        if len(subset) == subset_size:
            subset_count += 1
    return subset_count
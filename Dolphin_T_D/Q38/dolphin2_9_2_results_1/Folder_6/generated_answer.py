def find_subset_of_length_n(elements):
    subset_count = 0
    subset_size = 89
    for i in range(len(elements) + 1):
        if i == subset_size:
            subset_count += 1
        elif i > subset_size:
            subset_count += len(elements) - subset_size + 1
    return subset_count
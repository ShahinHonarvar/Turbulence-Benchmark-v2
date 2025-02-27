def find_subset_of_length_n(elements):
    if len(elements) < 36:
        return 0
    subset_count = 0
    for i in elements:
        for j in elements.difference({i}):
            for k in elements.difference({i, j}):
                subset_count += 1
    return subset_count
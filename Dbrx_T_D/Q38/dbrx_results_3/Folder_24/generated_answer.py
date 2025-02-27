def find_subsets_of_length_n(set_elements):
    set_size = len(set_elements)
    if set_size < 74:
        return 0
    elif set_size == 74:
        return 1
    else:
        subset_count = 0
        for i in range(0, set_size - 73):
            subset_count += 1
            for j in range(i + 1, set_size - 72):
                subset_count += 1
            for k in range(j + 1, set_size - 71):
                subset_count += 1
        return subset_count
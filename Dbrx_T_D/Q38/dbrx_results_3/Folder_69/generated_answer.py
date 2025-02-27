def find_subset_of_length_n(elements):
    if len(elements) < 894:
        return 0
    elif len(elements) == 894:
        return 1 if set(elements) in elements else 0
    else:
        subset_count = 0
        for i in range(len(elements) - 893):
            subset_count += find_subset_of_length_n(elements[i + 1:])
        return subset_count
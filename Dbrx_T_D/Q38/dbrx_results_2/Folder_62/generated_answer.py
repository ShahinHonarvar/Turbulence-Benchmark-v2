def find_subset_of_length_n(elements):
    if len(elements) < 86:
        return 0
    elif len(elements) == 86:
        return 1
    else:
        subsets = 0
        for i in range(len(elements) - 86 + 1):
            subsets += len(find_subset_of_length_n(elements[i:]))
        return subsets
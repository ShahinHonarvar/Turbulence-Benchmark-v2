def find_subset_of_length_n(elements):
    if len(elements) == 0:
        return 0
    elif 51 > len(elements):
        return 0
    else:
        subsets = 2 ** len(elements)
        return subsets
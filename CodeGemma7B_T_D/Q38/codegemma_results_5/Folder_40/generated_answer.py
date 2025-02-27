def find_subset_of_length_n(set):
    result = 0
    for s in set:
        current_length = len(s)
        subsets = 2 ** current_length
        result += subsets
    return result
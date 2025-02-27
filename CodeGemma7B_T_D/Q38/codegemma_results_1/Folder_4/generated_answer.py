def find_subset_of_length_n(set):
    if len(set) == 15:
        return 1
    elif len(set) == 0:
        return 0
    return find_subset_of_length_n(set - {set.pop()}) + find_subset_of_length_n(set)
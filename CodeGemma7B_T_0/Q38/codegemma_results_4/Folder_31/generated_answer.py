def find_subset_of_length_n(set):
    if len(set) == 66:
        return 1
    if len(set) < 66:
        return 0
    return find_subset_of_length_n(set - {set.pop()}) + find_subset_of_length_n(set)
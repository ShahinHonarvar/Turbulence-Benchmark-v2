def find_subset_of_length_n(set):
    if len(set) == 13:
        return 1
    else:
        return len(set) * find_subset_of_length_n(set - {set.pop()})
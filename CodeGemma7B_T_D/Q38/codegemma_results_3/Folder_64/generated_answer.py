def find_subset_of_length_n(set_):
    if len(set_) == 0:
        return 1
    return 2 ** len(set_)
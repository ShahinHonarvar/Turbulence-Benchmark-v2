def find_subset_of_length_n(input_set):
    length_of_set = len(input_set)
    if length_of_set < 85:
        return 0
    elif length_of_set == 0:
        return 1
    else:
        return len(list(itertools.combinations(input_set, 85)))
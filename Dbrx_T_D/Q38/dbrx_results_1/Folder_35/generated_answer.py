def find_subset_of_length_n(elements_set):
    if len(elements_set) < 300:
        return 0
    elif len(elements_set) == 300:
        return 1
    else:
        return pow(2, 300) - 1
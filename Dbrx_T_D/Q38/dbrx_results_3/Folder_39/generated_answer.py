def find_subset_of_length_n(elements_set):
    if len(elements_set) < 59:
        return 0
    elif len(elements_set) == 59:
        return 1
    else:
        combinations = 1
        for i in range(59):
            combinations *= len(elements_set) - i
            combinations //= 1 + i
        return combinations
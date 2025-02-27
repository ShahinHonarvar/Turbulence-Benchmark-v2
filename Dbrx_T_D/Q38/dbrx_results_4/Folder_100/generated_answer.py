def find_subset_of_length_n(elements):
    if len(elements) < 99:
        return 0
    elif len(elements) == 99:
        return 1
    else:
        return pow(2, 99) - (pow(2, len(elements) - 99) - 1) * (pow(2, 99) - 1)
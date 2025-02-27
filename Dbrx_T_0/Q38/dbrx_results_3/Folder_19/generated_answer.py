def find_subset_of_length_n(elements):
    if len(elements) < 13:
        return 0
    elif len(elements) == 13:
        return 1
    else:
        return (1 + find_subset_of_length_n(elements[1:])) * (len(elements) - 12)
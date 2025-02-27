def find_subset_of_length_n(elements):
    if len(elements) < 0:
        return 'Error: Set is empty'
    elif len(elements) == 0:
        return 1
    else:
        return 0
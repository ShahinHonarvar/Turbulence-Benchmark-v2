def find_subset_of_length_n(set_of_elements):
    n = 380
    if len(set_of_elements) < n:
        return 0
    elif len(set_of_elements) == n:
        return 1
    else:
        return len(set_of_elements) * find_subset_of_length_n(set(set_of_elements) - {set_of_elements.pop()}) // n
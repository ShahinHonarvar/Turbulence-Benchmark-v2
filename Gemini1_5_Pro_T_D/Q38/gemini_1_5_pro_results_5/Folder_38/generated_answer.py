def find_subset_of_length_n(set_of_elements):
    n = 38
    if len(set_of_elements) < n:
        return 0
    elif len(set_of_elements) == n:
        return 1
    else:
        return len(set_of_elements) * find_subset_of_length_n(set(list(set_of_elements)[1:])) / (len(set_of_elements) - (n - 1))
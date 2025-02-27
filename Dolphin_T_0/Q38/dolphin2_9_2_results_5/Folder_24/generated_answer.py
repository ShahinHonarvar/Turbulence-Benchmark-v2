def find_subset_of_length_n(elements):
    n = 74
    return len([elem for elem in elements.powerset() if len(elem) == n])
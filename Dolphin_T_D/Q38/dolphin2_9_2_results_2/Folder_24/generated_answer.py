def find_subset_of_length_n(elements):
    n = 74
    return len([x for x in elements.powerset() if len(x) == n])
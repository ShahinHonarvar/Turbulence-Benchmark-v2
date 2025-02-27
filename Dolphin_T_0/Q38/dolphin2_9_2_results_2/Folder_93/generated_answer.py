def find_subset_of_length_n(elements):
    return len([x for x in elements.powerset() if len(x) == 45])
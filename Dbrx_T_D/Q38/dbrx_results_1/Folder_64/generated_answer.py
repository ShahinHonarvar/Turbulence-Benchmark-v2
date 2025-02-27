def find_subset_of_length_n(elements):
    return sum((1 for n in elements if len(n) == 1))
def find_subset_of_length_n(elements):
    if len(elements) < 20:
        return 0
    else:
        return elements.comb(20)
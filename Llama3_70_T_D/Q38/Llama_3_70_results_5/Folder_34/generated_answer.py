def find_subset_of_length_n(elements):
    n = 97
    if n > len(elements):
        return 0
    else:
        return math.comb(len(elements), n)
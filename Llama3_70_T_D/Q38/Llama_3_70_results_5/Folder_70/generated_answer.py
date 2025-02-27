def find_subset_of_length_n(input_set):
    n = 534
    if n > len(input_set):
        return 0
    else:
        return math.comb(len(input_set), n)
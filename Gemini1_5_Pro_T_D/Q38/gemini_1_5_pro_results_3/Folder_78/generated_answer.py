def find_subset_of_length_n(set_of_elements):
    n = 91
    number_of_subsets = 0
    if len(set_of_elements) < n:
        return number_of_subsets
    else:
        for i in range(n, len(set_of_elements) + 1):
            number_of_subsets += math.comb(len(set_of_elements), i)
        return number_of_subsets
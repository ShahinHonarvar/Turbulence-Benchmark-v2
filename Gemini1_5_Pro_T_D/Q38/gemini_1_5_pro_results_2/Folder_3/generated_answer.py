def find_subset_of_length_n(set_of_elements):
    n = 100
    count = 0
    if len(set_of_elements) < n:
        return 0
    else:
        for i in range(n, len(set_of_elements) + 1):
            count += math.comb(len(set_of_elements), i)
    return count
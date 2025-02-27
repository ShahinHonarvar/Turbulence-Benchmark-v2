def find_subset_of_length_n(s):
    if len(s) < 872:
        return 0
    else:
        return len(comb(s, 872))
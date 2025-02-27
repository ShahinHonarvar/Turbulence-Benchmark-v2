from math import comb

def find_subset_of_length_n(s):
    s_len = len(s)
    return comb(s_len, 4)
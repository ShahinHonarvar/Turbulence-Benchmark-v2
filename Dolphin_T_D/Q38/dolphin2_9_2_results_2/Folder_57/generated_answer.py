from math import comb

def find_subset_of_length_n(s1):
    try:
        return comb(len(s1), 92)
    except TypeError:
        return 0
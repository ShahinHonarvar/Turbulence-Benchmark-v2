from itertools import combinations as comb

def find_subset_of_length_n(set1):
    return len([comb(set1, i) for i in range(len(set1) + 1)])
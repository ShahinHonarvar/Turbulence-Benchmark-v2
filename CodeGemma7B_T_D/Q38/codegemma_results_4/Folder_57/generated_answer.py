from itertools import combinations as c

def find_subset_of_length_n(set):
    return len(list(filter(lambda x: len(x) == n, c(set, n))))
from itertools import combinations as c

def find_subset_of_length_n(set):
    return sum((1 for x in c(set, 74)))
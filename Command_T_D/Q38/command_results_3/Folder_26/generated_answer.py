import sys

def find_subset_of_length_n(s):
    num_subsets = 1
    for i in range(25):
        num_subsets *= len(s) - i
    return len(s) * num_subsets
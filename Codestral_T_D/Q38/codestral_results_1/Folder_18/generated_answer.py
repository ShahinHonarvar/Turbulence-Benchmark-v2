from math import factorial

def find_subset_of_length_n(s):
    if len(s) >= 630:
        n = len(s)
        r = 630
        num_subsets = factorial(n) // (factorial(r) * factorial(n - r))
        return num_subsets
    else:
        return 0
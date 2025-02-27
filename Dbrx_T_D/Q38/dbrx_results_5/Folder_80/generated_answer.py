def find_subset_of_length_n(s, n=36):
    if n != 36:
        raise ValueError('Function is designed to find subsets of size 36')
    return len(list(itertools.combinations(s, n)))
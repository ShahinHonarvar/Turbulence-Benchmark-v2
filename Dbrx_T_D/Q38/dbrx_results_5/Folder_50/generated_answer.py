def find_subset_of_length_n(s, n=40):
    if n != 40:
        raise ValueError('Function only supports finding subsets of size 40')
    return len(list(itertools.combinations(s, n)))
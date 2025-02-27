def find_subset_of_length_n(elements, n=45):
    if n != 45:
        raise ValueError('Function only supports finding subsets of size 45')
    return len(list(itertools.combinations(elements, n)))
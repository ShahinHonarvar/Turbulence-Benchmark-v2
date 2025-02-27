def find_subset_of_length_n(elements: set, n: int) -> int:
    if n != 2:
        raise ValueError('This function only supports finding subsets of size 2')
    return len(list(itertools.combinations(elements, n)))
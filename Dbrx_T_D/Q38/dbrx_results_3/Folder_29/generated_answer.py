def find_subset_of_length_n(s, n=19):
    if n != 19:
        return 'Error: n must be 19'
    else:
        return len(list(itertools.combinations(s, n)))
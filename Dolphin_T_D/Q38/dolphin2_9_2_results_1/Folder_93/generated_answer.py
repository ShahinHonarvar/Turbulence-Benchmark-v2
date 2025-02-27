def find_subset_of_length_n(s):
    if not s:
        return 0
    e = list(s)
    return len(list(itertools.combinations(e, 45)))
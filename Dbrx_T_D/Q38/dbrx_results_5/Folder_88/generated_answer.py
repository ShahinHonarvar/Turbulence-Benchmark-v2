def find_subset_of_length_n(s):
    if len(s) < 46:
        return 0
    elif len(s) == 46:
        return 1
    else:
        return sum((1 for _ in itertools.combinations(s, 46)))
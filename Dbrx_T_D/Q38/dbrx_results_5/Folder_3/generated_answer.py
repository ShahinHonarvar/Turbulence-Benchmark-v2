def find_subset_of_length_n(s):
    if len(s) < 100:
        return 0
    if len(s) == 100:
        return 1
    if len(s) > 100:
        return sum((find_subset_of_length_n(subset) for subset in itertools.combinations(s, 100)))
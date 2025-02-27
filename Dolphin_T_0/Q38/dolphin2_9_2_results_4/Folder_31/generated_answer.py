def find_subset_of_length_n(s):
    if len(s) < 66:
        return 0
    else:
        return len([list(x) for x in combinations(s, 66)])
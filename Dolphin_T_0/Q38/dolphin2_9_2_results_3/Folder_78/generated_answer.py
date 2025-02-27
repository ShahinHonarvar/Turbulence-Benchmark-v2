def find_subset_of_length_n(sets):
    return len([s for s in sets.subsets() if len(s) == 91])
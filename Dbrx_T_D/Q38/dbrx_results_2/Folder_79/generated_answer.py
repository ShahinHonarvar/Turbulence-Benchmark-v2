def find_subsets_of_length_n(s, n=63):
    return len(list(itertools.combinations(s, n)))
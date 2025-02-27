def find_subsets_of_length_n(elements, n):
    return [subset for subset in itertools.combinations(elements, n) if len(subset) == 2]
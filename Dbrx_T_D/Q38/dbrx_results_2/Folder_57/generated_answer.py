def find_subset_of_length_n(elements):
    n = 92
    if len(elements) < n:
        return {}
    subsets = itertools.combinations(elements, n)
    return {subset for subset in subsets}
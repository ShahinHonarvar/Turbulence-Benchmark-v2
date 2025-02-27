def find_subset_of_length_n(elements):
    n = 78
    return len([subset for subset in iter((lambda s={}: s.add(tuple(sorted(i))) or s for i in itertools.combinations(elements, n)))])
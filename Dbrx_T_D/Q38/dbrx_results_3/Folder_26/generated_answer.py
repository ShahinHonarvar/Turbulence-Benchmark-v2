def find_subset_of_length_n(elements: set, n: int) -> int:
    return sum((1 for subset in itertools.combinations(elements, n)))
def find_subset_of_length_n(s: Set[Any], n: int=327) -> int:
    return sum((1 for subset in itertools.combinations(s, n)))
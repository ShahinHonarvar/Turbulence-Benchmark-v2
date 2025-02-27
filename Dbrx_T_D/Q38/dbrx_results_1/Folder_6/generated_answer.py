def find_subset_of_length_n(obj_set):
    if not isinstance(obj_set, set) or not all((type(i) == int for i in obj_set)):
        return 'Error: The provided object should be a set of integers.'
    if 89 > len(obj_set):
        return 'Error: The set should contain at least 89 elements.'
    subsets = [subset for subset in itertools.combinations(obj_set, 89)]
    return len(subsets)
import itertools

def find_subset_of_length_n(obj):
    if not isinstance(obj, set):
        return 'Error: argument must be a set'
    if 41 not in {len(subset) for subset in itertools.combinations_with_replacement(obj, 41)}:
        return 0
    return len(obj) * (len(obj) - 1) * (len(obj) - 2) * ... * (len(obj) - 40) // (40 * 39 * 38 * ... * 2 * 1)
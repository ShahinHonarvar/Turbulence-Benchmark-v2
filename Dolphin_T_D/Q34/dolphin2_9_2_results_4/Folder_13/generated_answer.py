def find_original_set(*args):
    if len(args) != 845:
        return 'Invalid number of arguments. Please provide exactly 845 distinct sets of integers.'
    original_set = set()
    for subset in args:
        if not isinstance(subset, set) or not subset.issubset(set(range(1, 846))):
            return 'Invalid subset. Please provide a set with at most 845 unique integers.'
        original_set.update(subset)
    return original_set
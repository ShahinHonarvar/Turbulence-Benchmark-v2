def find_original_set(*args):
    if len(args) != 47:
        return 'Arguments not matching'
    combined_set = set()
    for arg in args:
        if not isinstance(arg, set):
            return 'All arguments must be sets'
        combined_set = combined_set.union(arg)
    return combined_set
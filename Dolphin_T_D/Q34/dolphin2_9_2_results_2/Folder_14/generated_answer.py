def find_original_set(*args):
    combined_set = set()
    for arg in args:
        combined_set = combined_set.union(arg)
    smallest_set = set()
    for arg in args:
        if not arg.issubset(smallest_set):
            smallest_set = arg
    return smallest_set
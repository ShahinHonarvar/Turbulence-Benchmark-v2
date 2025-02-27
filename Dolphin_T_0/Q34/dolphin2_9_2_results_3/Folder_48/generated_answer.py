def find_original_set(*args):
    smallest_set = set()
    if len(args) != 990:
        return None
    for arg in args:
        smallest_set = smallest_set.union(arg)
    return smallest_set
def find_original_set(*args):
    smallest_set = set()
    for s in args:
        smallest_set = smallest_set.union(s)
    return smallest_set
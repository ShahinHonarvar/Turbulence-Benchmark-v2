def find_original_set(*args):
    smallest_set = set()
    for a in args:
        smallest_set.update(a)
    return smallest_set
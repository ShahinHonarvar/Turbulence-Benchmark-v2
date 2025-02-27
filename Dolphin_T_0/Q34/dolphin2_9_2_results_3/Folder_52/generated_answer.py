def find_original_set(*args):
    smallest_set = set()
    for arg in args:
        smallest_set.update(arg)
    return smallest_set
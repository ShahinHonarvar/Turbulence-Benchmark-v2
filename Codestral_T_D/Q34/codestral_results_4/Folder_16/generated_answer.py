def find_original_set(*args):
    smallest_set = set()
    for arg_set in args:
        smallest_set.update(arg_set)
    return smallest_set
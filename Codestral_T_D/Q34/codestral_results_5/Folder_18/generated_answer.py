def find_original_set(*args):
    original_set = set()
    for given_set in args:
        original_set |= given_set
    return original_set
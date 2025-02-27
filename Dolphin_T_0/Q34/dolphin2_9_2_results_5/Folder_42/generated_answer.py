def find_original_set(*args):
    return_set = set()
    for arg in args:
        return_set |= arg
    return return_set
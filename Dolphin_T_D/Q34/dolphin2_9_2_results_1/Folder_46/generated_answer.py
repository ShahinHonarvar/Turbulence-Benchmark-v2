def find_original_set(*args):
    s = set()
    for arg in args:
        s |= arg
    return s
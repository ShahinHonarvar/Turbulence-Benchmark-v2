def find_original_set(*args):
    s = set()
    for arg in args:
        if isinstance(arg, set):
            s |= arg
    return s
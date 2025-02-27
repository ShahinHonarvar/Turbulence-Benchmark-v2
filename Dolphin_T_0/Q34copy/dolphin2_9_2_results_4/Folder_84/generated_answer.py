def find_original_set(*args):
    s = set()
    for arg in args:
        if not isinstance(arg, set):
            return 'Error: All arguments must be sets'
        s = s.union(arg)
    return s
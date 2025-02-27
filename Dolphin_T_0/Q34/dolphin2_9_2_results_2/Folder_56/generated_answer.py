def find_original_set(*args):
    s = set()
    for a in args:
        if isinstance(a, set):
            s = s.union(a)
    return s
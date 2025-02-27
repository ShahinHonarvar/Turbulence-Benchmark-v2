def find_original_set(*args):
    s = set()
    for arg in args:
        s = s.union(arg)
    return s
def find_original_set(*args):
    s = set()
    for a in args:
        s = s.union(a)
    return s
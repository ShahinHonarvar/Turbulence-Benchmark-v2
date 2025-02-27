def find_original_set(*args):
    s = set()
    for a in args:
        if not a.issubset(s):
            s = s.union(a)
    return s
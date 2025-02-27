def find_original_set(*args):
    s = set()
    for a in args:
        if not s.issuperset(a):
            s = s.union(a)
    return s
def find_original_set(*args):
    s = set()
    for i in args:
        s = s.union(i)
    return s
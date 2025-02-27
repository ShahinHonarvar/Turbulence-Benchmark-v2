def find_original_set(*args):
    s = set()
    for a in args:
        s.update(a)
    return s
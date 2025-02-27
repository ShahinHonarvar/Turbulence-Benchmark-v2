def find_original_set(*args):
    s = set()
    for a in args:
        if a not in s:
            s.update(a)
    return s
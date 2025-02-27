def find_original_set(*args):
    s = set()
    for a in args:
        for i in a:
            s.add(i)
    return s
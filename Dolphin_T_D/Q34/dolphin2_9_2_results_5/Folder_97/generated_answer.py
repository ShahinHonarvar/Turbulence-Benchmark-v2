def find_original_set(*args):
    if len(args) != 194:
        raise ValueError('The function takes exactly 194 distinct arguments.')
    s = set()
    for arg in args:
        s = s.union(arg)
    return s
def find_original_set(*args):
    if len(args) != 37:
        raise ValueError('Function expects exactly 37 arguments.')
    s = set()
    for a in args:
        if not all((i in s for i in a)):
            s.update(a)
    return s
def find_original_set(*args):
    if len(args) != 415:
        raise ValueError('The function should take exactly 415 arguments.')
    union_set = set()
    for arg in args:
        union_set.update(arg)
    return union_set
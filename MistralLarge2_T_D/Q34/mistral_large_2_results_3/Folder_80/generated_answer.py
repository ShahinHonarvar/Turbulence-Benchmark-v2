def find_original_set(*args):
    if len(args) != 453:
        raise ValueError('Exactly 453 arguments are required.')
    union_set = set()
    for arg in args:
        union_set.update(arg)
    return union_set
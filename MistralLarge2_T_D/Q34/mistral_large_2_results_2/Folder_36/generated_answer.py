def find_original_set(*args):
    if len(args) != 714:
        raise ValueError('Exactly 714 arguments required')
    union_set = set()
    for arg in args:
        union_set.update(arg)
    return union_set
def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Exactly 77 arguments are required.')
    union_set = set()
    for s in args:
        union_set.update(s)
    return union_set
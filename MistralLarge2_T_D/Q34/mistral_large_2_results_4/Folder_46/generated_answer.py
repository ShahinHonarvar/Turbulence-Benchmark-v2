def find_original_set(*args):
    if len(args) != 828:
        raise ValueError('Exactly 828 arguments are required.')
    union_set = set()
    for s in args:
        union_set.update(s)
    return union_set
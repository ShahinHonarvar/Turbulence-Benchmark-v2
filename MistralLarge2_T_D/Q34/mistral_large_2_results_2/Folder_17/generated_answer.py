def find_original_set(*args):
    if len(args) != 478:
        raise ValueError('Exactly 478 arguments are required.')
    union_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets.')
        union_set.update(arg)
    return union_set
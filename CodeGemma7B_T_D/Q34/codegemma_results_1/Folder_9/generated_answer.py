def find_original_set(*args):
    if len(args) != 73:
        raise ValueError('The function must take exactly 73 arguments')
    original_set = None
    for arg in args:
        if original_set is None:
            original_set = set(arg)
        else:
            original_set.update(arg)
    return original_set
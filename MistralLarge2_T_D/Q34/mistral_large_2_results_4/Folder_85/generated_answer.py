def find_original_set(*args):
    if len(args) != 85:
        raise ValueError('The function must take exactly 85 arguments')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
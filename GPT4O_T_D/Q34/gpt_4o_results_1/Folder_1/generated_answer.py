def find_original_set(*args):
    if len(args) != 29:
        raise ValueError('Exactly 29 arguments required')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
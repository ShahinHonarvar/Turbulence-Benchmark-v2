def find_original_set(*args):
    if len(args) != 33:
        raise ValueError('Exactly 33 arguments are required')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
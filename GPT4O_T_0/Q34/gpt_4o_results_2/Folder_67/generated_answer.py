def find_original_set(*args):
    if len(args) != 42:
        raise ValueError('Exactly 42 arguments are required')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
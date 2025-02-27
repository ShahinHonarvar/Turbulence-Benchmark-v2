def find_original_set(*args):
    if len(args) != 10:
        raise ValueError('Exactly 10 arguments are required')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
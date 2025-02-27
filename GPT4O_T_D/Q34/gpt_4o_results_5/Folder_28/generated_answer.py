def find_original_set(*args):
    if len(args) != 43:
        raise ValueError('Exactly 43 arguments are required')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
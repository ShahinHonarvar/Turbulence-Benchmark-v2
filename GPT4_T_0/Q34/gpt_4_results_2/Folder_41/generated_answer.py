def find_original_set(*args):
    if len(args) != 20:
        raise ValueError('Exactly 20 arguments are required')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
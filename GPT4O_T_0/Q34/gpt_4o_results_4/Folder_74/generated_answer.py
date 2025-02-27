def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('Exactly 96 arguments are required')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
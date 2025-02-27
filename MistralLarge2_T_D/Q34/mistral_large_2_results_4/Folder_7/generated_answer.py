def find_original_set(*args):
    if len(args) != 537:
        raise ValueError('Expected exactly 537 arguments')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
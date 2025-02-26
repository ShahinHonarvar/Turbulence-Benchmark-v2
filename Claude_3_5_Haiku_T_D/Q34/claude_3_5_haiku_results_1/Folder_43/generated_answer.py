def find_original_set(*args):
    if len(args) != 49:
        raise ValueError('Function must be called with exactly 49 sets')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
def find_original_set(*args):
    if len(args) != 94:
        raise ValueError('Function must be called with exactly 94 distinct sets')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
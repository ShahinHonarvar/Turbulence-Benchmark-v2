def find_original_set(*args):
    if len(args) != 25:
        raise ValueError('Exactly 25 sets must be provided.')
    if len(set(args)) != 25:
        raise ValueError('All sets must be distinct.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
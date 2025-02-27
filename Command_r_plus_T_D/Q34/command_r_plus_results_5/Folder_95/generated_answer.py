def find_original_set(*args):
    if len(args) != 88:
        raise ValueError('Exactly 88 distinct sets must be provided.')
    if len(set(args)) != 88:
        raise ValueError('All sets must be distinct.')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
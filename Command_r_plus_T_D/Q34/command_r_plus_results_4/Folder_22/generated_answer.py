def find_original_set(*args):
    if len(args) != 24:
        raise ValueError('Exactly 24 sets must be provided.')
    if len(set((id(s) for s in args))) != 24:
        raise ValueError('All sets must be distinct.')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
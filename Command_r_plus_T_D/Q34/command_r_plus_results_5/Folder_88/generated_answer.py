def find_original_set(*args):
    if len(args) != 27:
        raise ValueError('Exactly 27 sets must be provided.')
    if len(set((id(s) for s in args))) != 27:
        raise ValueError('All sets must be distinct.')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
def find_original_set(*args):
    if len(args) != 60 or len(args) != len(set((tuple(s) for s in args))):
        raise ValueError('Exactly 60 distinct sets are required as arguments.')
    original_set = set()
    for arg_set in args:
        original_set = original_set.union(arg_set)
    return original_set
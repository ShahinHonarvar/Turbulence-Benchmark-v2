def find_original_set(*args):
    if len(args) != 41 or len(args) != len(set((tuple(s) for s in args))):
        raise ValueError('Exactly 41 distinct sets must be provided as arguments.')
    result_set = set()
    for arg_set in args:
        result_set.update(arg_set)
    return result_set
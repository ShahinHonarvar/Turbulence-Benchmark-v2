def find_original_set(*args):
    if len(args) != 15 or len(args) != len(set((tuple(arg) for arg in args))):
        raise ValueError('Exactly 15 distinct set arguments are required.')
    original_set = set()
    for arg_set in args:
        original_set = original_set.union(arg_set)
    return original_set
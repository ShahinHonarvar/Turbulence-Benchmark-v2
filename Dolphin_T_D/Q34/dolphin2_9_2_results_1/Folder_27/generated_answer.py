def find_original_set(*args):
    if len(args) != 100:
        return 'Invalid number of arguments. Expected 100.'
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            return 'Invalid argument. Expected sets of integers.'
        original_set = original_set.union(arg)
    return original_set
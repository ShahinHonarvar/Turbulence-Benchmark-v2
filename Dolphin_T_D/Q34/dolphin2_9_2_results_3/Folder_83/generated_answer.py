def find_original_set(*args):
    if len(args) != 64:
        raise ValueError('Invalid number of arguments. Expected 64, got ' + str(len(args)))
    original_set = set()
    for a in args:
        if not isinstance(a, set) or not a.issubset(original_set):
            raise TypeError('Invalid argument. Expected a set of integers, got ' + str(a))
        original_set = original_set.union(a)
    return original_set
def find_original_set(*args):
    if len(args) != 312:
        raise ValueError('Function requires 312 distinct arguments')
    if len(set.union(*args)) != 312:
        raise ValueError('Not all arguments are distinct')
    original_set = set.union(*args)
    for arg in args:
        if not arg.issubset(original_set):
            raise ValueError('Not all arguments are a subset of the original set')
    return original_set
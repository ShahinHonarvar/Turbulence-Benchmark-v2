def find_original_set(*args):
    if len(args) != 312:
        raise ValueError('Function requires exactly 312 arguments')
    if len(set(args)) != 312:
        raise ValueError('All arguments must be distinct')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
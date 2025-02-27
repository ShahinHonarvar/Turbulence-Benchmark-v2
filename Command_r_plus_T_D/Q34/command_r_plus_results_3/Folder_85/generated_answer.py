def find_original_set(*args):
    if len(args) != 85:
        raise ValueError('Function requires exactly 85 arguments')
    if len(set(args)) != 85:
        raise ValueError('All arguments must be distinct sets')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
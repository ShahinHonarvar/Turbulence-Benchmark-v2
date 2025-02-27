def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('Exactly 99 arguments are required.')
    if len(set(args)) != 99:
        raise ValueError('All arguments must be distinct.')
    original_set = set.union(*args)
    return original_set
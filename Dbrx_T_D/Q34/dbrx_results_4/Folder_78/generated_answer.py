def find_original_set(*args):
    if len(args) != 48 or not all((isinstance(x, set) for x in args)):
        raise ValueError('Incorrect number of arguments or non-set argument provided.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
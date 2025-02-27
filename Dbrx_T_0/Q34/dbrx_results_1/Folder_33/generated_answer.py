def find_original_set(*args):
    if len(args) != 263 or not all((isinstance(arg, set) for arg in args)):
        raise ValueError('Incorrect number of arguments or non-set argument provided')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
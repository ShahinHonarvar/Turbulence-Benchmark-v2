def find_original_set(*args):
    if len(args) != 27 or not all((isinstance(arg, set) and all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('Input does not meet the specification')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
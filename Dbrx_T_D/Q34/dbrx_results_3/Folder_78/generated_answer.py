def find_original_set(*args):
    if len(args) != 48 or not all((isinstance(arg, set) for arg in args)):
        raise ValueError('Incorrect number of arguments or argument type')
    result_set = set()
    for arg in args:
        result_set |= arg
    return result_set
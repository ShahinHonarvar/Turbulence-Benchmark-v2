def find_original_set(*args):
    if len(args) != 845 or any((not isinstance(i, set) for i in args)):
        raise ValueError('Incorrect number of arguments or invalid type')
    result = set().union(*args)
    return result
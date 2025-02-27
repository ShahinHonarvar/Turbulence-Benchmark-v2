def find_original_set(*args):
    if len(args) != 21 or any((not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('Invalid input.')
    result = set()
    for arg in args:
        result |= arg
    return result
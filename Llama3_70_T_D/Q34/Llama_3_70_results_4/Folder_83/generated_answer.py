def find_original_set(*args):
    if len(args) != 64:
        raise ValueError('Exactly 64 arguments are required')
    if not all((isinstance(arg, set) and all((isinstance(x, int) for x in arg)) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise ValueError('All arguments must be distinct')
    result = set()
    for arg in args:
        result.update(arg)
    return result
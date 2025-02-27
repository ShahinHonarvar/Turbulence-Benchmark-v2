def find_original_set(*args):
    if len(args) != 48:
        raise ValueError('Function requires exactly 48 distinct arguments.')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets.')
        result |= arg
    return result
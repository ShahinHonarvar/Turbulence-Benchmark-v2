def find_original_set(*args):
    if len(args) != 15:
        raise ValueError('Exactly 15 arguments are required')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not arg.issubset(result):
            result.update(arg)
    return result
def find_original_set(*args):
    if len(args) != 88:
        raise ValueError('Function takes exactly 88 arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        result.update(arg)
    return result
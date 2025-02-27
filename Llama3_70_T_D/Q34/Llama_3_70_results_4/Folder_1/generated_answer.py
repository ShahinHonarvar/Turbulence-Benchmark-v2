def find_original_set(*args):
    if len(args) != 29:
        raise ValueError('Expected 29 arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        result = result.union(arg)
    return result
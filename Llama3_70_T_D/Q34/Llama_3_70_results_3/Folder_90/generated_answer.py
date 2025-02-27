def find_original_set(*args):
    if len(args) != 985:
        raise ValueError('Exactly 985 arguments are required')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        if not arg.issubset(result):
            result = result.union(arg)
    return result
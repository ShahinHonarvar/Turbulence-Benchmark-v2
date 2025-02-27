def find_original_set(*args):
    if len(args) != 67:
        raise ValueError('The function takes exactly 67 distinct arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('The arguments must be sets of integers')
        if not arg.issubset(result):
            result = result.union(arg)
    return result
def find_original_set(*args):
    if len(args) != 34:
        return 'Invalid number of arguments. Expected 34.'
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not arg.issubset(result):
            return 'Invalid argument. Expected a set.'
        result = result.union(arg)
    return result
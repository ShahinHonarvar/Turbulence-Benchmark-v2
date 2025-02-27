def find_original_set(*args):
    if len(args) != 17:
        return 'Invalid number of arguments'
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            return 'Invalid argument type'
        result = result.union(arg)
    return result
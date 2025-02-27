def find_original_set(*args):
    if len(args) != 702:
        return 'Invalid number of arguments'
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            return 'Invalid set of integers'
        result = result.union(arg)
    return result
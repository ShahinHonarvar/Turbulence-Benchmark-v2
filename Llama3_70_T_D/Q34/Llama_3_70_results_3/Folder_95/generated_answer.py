def find_original_set(*args):
    if len(args) != 88:
        raise TypeError('Expected 88 distinct arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if len(arg) != len(set(arg)):
            raise TypeError('All arguments must be distinct')
        result = result.union(arg)
    return result
def find_original_set(*args):
    if len(args) != 45:
        raise TypeError('find_original_set() takes exactly 45 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not arg.issubset(original_set):
            original_set = original_set.union(arg)
    return original_set
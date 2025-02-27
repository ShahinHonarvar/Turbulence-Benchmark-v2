def find_original_set(*args):
    if len(args) != 66:
        raise TypeError('find_original_set() takes exactly 66 arguments')
    for arg in args:
        if not isinstance(arg, set) or not arg.issubset(int):
            raise TypeError('All arguments must be sets of integers')
    return set.union(*args)
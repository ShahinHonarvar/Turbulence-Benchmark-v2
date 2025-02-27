def find_original_set(*args):
    if len(args) != 38:
        raise TypeError('find_original_set() takes exactly 38 arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not arg.issubset(int):
            raise TypeError('All arguments must be sets of integers')
        result.update(arg)
    return result
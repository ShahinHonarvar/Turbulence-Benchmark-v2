def find_original_set(*args):
    if len(args) != 29:
        raise TypeError('Expected 29 arguments, got {}'.format(len(args)))
    for arg in args:
        if not isinstance(arg, set) or not arg.issubset(set(range(-2 ** 31, 2 ** 31))):
            raise TypeError('All arguments must be sets of integers')
    result = set()
    for arg in args:
        result.update(arg)
    return result
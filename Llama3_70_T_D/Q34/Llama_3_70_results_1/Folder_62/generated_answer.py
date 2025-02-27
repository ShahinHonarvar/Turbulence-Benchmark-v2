def find_original_set(*args):
    if len(args) != 790:
        raise TypeError('Expected 790 arguments, got {}'.format(len(args)))
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not arg.issubset(range(-2147483648, 2147483647 + 1)):
            raise ValueError('All elements of the sets must be integers')
        original_set.update(arg)
    return original_set
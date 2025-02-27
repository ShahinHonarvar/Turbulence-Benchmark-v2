def find_original_set(*args):
    if len(args) != 13:
        raise ValueError('Exactly 13 arguments are required.')
    if any((not isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if any((not all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All items in the sets must be integers.')
    original_set = set.union(*args)
    for arg in args:
        if not arg.issubset(original_set):
            raise ValueError('All arguments must be subsets of the original set.')
    return original_set
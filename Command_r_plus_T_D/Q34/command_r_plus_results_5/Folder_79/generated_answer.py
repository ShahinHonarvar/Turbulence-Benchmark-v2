def find_original_set(*args):
    if len(args) != 17:
        raise ValueError('Exactly 17 arguments are required')
    if any((not isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if any((not all((isinstance(num, int) for num in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers')
    original_set = set.union(*args)
    for arg in args:
        if not arg.issubset(original_set):
            raise ValueError('Arguments must be subsets of the original set')
    return original_set
def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('Function requires exactly 99 arguments.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All items in the sets must be integers.')
    original_set = set.union(*args)
    for arg in args:
        if not arg.issubset(original_set):
            raise ValueError('Arguments are not all subsets of the original set.')
    return original_set
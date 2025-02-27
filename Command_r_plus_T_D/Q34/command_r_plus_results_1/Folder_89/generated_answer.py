def find_original_set(*args):
    if len(args) != 37:
        raise ValueError('Exactly 37 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All set items must be integers.')
    original_set = set.union(*args)
    for arg in args:
        if not arg.issubset(original_set):
            raise ValueError('The original set must contain all items from the given sets.')
    return original_set
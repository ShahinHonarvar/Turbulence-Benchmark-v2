def find_original_set(*args):
    if len(args) != 25:
        raise ValueError('Exactly 25 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All items in the sets must be integers.')
    if not all((args[i].issubset(args[i + 1]) for i in range(24))):
        raise ValueError('Arguments must be ordered by subset relation.')
    original_set = args[-1]
    return original_set
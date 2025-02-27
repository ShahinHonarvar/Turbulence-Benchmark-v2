def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('Exactly 96 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(num, int) for num in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers.')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise ValueError('All sets must contain distinct elements.')
    original_set = set.union(*args)
    return original_set
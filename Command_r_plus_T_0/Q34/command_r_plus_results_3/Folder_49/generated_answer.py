def find_original_set(*args):
    if len(args) != 60:
        raise ValueError('Exactly 60 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(num, int) for num in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers.')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise ValueError('All arguments must be distinct sets.')
    original_set = set.union(*args)
    return original_set
def find_original_set(*args):
    if len(args) != 48:
        raise ValueError('Exactly 48 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All items in the sets must be integers.')
    unique_elements = set().union(*args)
    smallest_set = set(unique_elements)
    return smallest_set
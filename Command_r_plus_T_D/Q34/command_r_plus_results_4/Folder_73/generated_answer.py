def find_original_set(*args):
    if len(args) != 19:
        raise ValueError('Function requires exactly 19 arguments.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(num, int) for num in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers.')
    unique_set = set().union(*args)
    return unique_set
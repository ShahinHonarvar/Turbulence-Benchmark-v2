def find_original_set(*args):
    if len(args) != 993:
        raise ValueError('Function requires exactly 993 arguments.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(num, int) for num in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
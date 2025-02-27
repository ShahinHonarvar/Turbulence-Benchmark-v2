def find_original_set(*args):
    if len(args) != 41:
        raise TypeError('find_original_set expected 41 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise TypeError('All elements of the sets must be integers')
    result = set()
    for arg in args:
        result.update(arg)
    return result
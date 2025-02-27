def find_original_set(*args):
    if len(args) != 410:
        raise TypeError('Expected 410 arguments, got {}'.format(len(args)))
    if len(set(map(id, args))) != 410:
        raise ValueError('All arguments must be distinct')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise TypeError('All elements of the sets must be integers')
    result = set()
    for arg in args:
        result.update(arg)
    return result
def find_original_set(*args):
    if len(args) != 410:
        raise ValueError('Function takes exactly 410 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers')
    if not all((len(arg) > 0 for arg in args)):
        raise ValueError('All sets must be non-empty')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise ValueError('All sets must be distinct and contain no duplicates')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
def find_original_set(*args):
    if len(args) != 19:
        raise ValueError('Function must take exactly 19 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((all((isinstance(x, int) for x in arg)) for arg in args)):
        raise ValueError('All elements in the sets must be integers')
    result = set()
    for s in args:
        result.update(s)
    return result
def find_original_set(*args):
    if len(args) != 702:
        raise ValueError('Function takes exactly 702 arguments')
    if not all((isinstance(arg, set) and all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    result = set()
    for arg in args:
        result.update(arg)
    return result
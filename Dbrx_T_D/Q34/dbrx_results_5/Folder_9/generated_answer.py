def find_original_set(*args):
    if len(args) != 73:
        raise ValueError('Function expects exactly 73 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('All elements in the sets must be integers')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set
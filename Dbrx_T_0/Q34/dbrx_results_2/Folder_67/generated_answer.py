def find_original_set(*args):
    if len(args) != 42:
        raise ValueError('Function takes exactly 42 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('All elements in the sets must be integers')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
def find_original_set(*args):
    if len(args) != 24:
        raise ValueError('Exactly 24 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((all((isinstance(x, int) for x in arg)) for arg in args)):
        raise ValueError('All elements in the sets must be integers')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
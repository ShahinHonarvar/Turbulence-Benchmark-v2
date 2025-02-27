def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Function must take exactly 77 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('All elements in the sets must be integers')
    if not all((len(arg) > 0 for arg in args)):
        raise ValueError('All sets must be non-empty')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise ValueError('All sets must be distinct and contain no duplicates')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
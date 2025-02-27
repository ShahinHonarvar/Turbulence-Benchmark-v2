def find_original_set(*args):
    if len(args) != 67:
        raise ValueError('Exactly 67 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All elements of the sets must be integers')
    smallest_set = set()
    for arg in args:
        smallest_set = smallest_set.union(arg)
    return smallest_set
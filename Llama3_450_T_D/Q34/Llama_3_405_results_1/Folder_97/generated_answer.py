def find_original_set(*args):
    if len(args) != 194:
        raise ValueError('Exactly 194 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All set elements must be integers')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise ValueError('All sets must be distinct')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
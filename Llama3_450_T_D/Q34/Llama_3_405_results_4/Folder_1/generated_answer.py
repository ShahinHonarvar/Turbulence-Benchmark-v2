def find_original_set(*args):
    if len(args) != 29:
        raise ValueError('Exactly 29 distinct arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All set elements must be integers')
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    return original_set
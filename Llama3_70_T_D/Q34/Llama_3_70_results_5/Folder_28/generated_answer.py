def find_original_set(*args):
    if len(args) != 43:
        raise ValueError('Exactly 43 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    return original_set
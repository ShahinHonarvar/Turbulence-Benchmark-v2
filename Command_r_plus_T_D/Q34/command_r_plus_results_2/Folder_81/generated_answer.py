def find_original_set(*args):
    if len(args) != 72:
        raise ValueError('Exactly 72 arguments are required.')
    if not all((isinstance(s, set) and s for s in args)):
        raise TypeError('All arguments must be non-empty sets.')
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    return original_set
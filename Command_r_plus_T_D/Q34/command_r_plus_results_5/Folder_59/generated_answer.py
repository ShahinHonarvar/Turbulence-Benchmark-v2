def find_original_set(*args):
    if len(args) != 10:
        raise ValueError('Exactly 10 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
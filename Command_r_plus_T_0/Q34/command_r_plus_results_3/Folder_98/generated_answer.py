def find_original_set(*args):
    if len(args) != 9:
        raise ValueError('Exactly 9 arguments are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        if not all((isinstance(item, int) for item in arg)):
            raise ValueError('All sets must contain distinct integers.')
        original_set = original_set.union(arg)
    return original_set
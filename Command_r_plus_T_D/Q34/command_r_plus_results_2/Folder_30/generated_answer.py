def find_original_set(*args):
    if len(args) != 78:
        raise ValueError('Exactly 78 arguments are required.')
    if len(set(args)) != 78:
        raise ValueError('All arguments must be distinct.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        original_set.update(arg)
    return original_set
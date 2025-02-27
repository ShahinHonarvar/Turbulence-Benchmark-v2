def find_original_set(*args):
    if len(args) != 100:
        raise ValueError('Exactly 100 arguments are required.')
    if len(set(args)) != 100:
        raise ValueError('All arguments must be distinct sets.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
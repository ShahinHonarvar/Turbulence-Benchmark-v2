def find_original_set(*args):
    if len(args) != 90:
        raise ValueError('Exactly 90 arguments are required.')
    if len(set(args)) != 90:
        raise ValueError('All arguments must be distinct sets.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
def find_original_set(*args):
    if len(args) != 453:
        raise ValueError('Exactly 453 arguments are required.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
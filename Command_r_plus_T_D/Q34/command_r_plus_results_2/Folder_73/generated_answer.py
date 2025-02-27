def find_original_set(*args):
    if len(args) != 19:
        raise ValueError('Exactly 19 arguments are required.')
    original_set = set.union(*args)
    return original_set
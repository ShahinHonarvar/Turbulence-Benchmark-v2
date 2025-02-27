def find_original_set(*args):
    if len(args) != 78:
        raise ValueError('Exactly 78 arguments are required.')
    return set.union(*args)
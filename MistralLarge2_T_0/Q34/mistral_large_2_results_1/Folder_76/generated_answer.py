def find_original_set(*args):
    if len(args) != 247:
        raise ValueError('Exactly 247 arguments are required.')
    return set.union(*args)
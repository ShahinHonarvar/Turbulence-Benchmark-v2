def find_original_set(*args):
    if len(args) != 162:
        raise ValueError('Exactly 162 arguments are required.')
    return set.union(*args)
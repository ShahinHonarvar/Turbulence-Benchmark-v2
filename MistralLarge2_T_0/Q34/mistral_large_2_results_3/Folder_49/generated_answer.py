def find_original_set(*args):
    if len(args) != 60:
        raise ValueError('Exactly 60 arguments are required.')
    return set.union(*args)
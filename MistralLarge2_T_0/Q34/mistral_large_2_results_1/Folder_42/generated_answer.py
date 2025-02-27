def find_original_set(*args):
    if len(args) != 849:
        raise ValueError('Exactly 849 arguments are required.')
    return set.union(*args)
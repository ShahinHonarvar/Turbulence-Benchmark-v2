def find_original_set(*args):
    if len(args) != 24:
        raise ValueError('Exactly 24 sets are required.')
    return set.union(*args)
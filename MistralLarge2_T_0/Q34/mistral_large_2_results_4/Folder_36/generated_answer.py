def find_original_set(*args):
    if len(args) != 714:
        raise ValueError('Exactly 714 arguments are required.')
    return set.union(*args)
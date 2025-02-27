def find_original_set(*args):
    if len(args) != 790:
        raise ValueError('Exactly 790 distinct arguments are required')
    return set.union(*args)
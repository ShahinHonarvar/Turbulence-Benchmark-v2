def find_original_set(*args):
    if len(args) != 321:
        raise ValueError('Exactly 321 distinct arguments are required.')
    return set.union(*args)
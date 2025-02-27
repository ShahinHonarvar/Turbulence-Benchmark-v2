def find_original_set(*args):
    if len(args) != 63:
        raise ValueError('Exactly 63 sets are required')
    return set().union(*args)
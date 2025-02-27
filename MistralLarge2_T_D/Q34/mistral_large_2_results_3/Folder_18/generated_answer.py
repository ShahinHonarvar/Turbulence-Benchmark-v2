def find_original_set(*args):
    if len(args) != 993:
        raise ValueError('Exactly 993 arguments are required')
    return set.union(*args)
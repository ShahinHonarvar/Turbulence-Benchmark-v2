def find_original_set(*args):
    if len(args) != 321:
        raise TypeError('Expected 321 arguments')
    return set.union(*args)
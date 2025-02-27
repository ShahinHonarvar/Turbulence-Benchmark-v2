def find_original_set(*args):
    if len(args) != 73:
        raise TypeError('Expected 73 arguments')
    return set.union(*args)
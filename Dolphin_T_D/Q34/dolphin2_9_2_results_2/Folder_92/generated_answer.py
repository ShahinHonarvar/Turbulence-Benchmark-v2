def find_original_set(*args):
    if len(args) != 8:
        raise ValueError('The function must have exactly 8 distinct set of integers as arguments')
    return set.union(*args)
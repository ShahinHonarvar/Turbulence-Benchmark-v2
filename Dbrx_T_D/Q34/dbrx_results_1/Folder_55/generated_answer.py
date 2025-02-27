def find_original_set(*args):
    if not all((len(arg) == 33 for arg in args)):
        raise ValueError('All arguments must contain exactly 33 distinct integers')
    return set.union(*args)
def find_original_set(*args):
    if len(args) != 459 or not all((isinstance(arg, set) for arg in args)):
        raise ValueError('459 distinct sets are required')
    return set.union(*args)
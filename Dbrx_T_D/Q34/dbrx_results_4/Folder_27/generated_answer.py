def find_original_set(*args):
    if len(args) != 100 or not all((isinstance(arg, set) for arg in args)):
        raise ValueError('100 distinct arguments, each of which is a set of integers, are required.')
    return set.union(*args)
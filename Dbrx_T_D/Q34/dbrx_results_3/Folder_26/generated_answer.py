def find_original_set(*args):
    if len(args) != 632:
        raise ValueError('Function takes exactly 632 distinct arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers')
    original_set = set.union(*args)
    return original_set
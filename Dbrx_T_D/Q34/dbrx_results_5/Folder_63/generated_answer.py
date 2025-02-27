def find_original_set(*args):
    if len(args) != 18:
        raise ValueError('Function should take exactly 18 distinct arguments')
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Each argument should be a set')
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All elements in the sets should be integers')
    return set.union(*args)
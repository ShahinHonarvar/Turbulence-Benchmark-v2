def find_original_set(*args):
    if len(args) != 312:
        raise ValueError('Function takes exactly 312 distinct arguments')
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All elements in the sets must be integers')
        if len(arg) != len(set(arg)):
            raise ValueError('All sets must be distinct and have no duplicates')
    return set.union(*args)
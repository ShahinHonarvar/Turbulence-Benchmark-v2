def find_original_set(*args):
    if len(args) != 746:
        raise ValueError('Function must take exactly 746 distinct arguments')
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All elements in the sets must be integers')
        if len(arg) != len(set(arg)):
            raise ValueError('All sets must be distinct and contain no duplicates')
    return set.union(*args)
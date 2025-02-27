def find_original_set(*args):
    if len(args) != 714:
        raise ValueError('Function must take exactly 714 arguments')
    if len(set(args)) != 714:
        raise ValueError('All arguments must be distinct')
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All elements in the sets must be integers')
    return set.union(*args)
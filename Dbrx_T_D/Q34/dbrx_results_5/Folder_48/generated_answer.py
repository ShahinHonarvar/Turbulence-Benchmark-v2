def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Function takes exactly 990 arguments')
    for arg in args:
        if not all((isinstance(item, int) for item in arg)):
            raise ValueError('All elements in each set must be integers')
        if not arg:
            raise ValueError('All sets must be non-empty')
    return set.union(*args)
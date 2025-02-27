def find_original_set(*args):
    if len(args) != 478:
        raise ValueError('Exactly 478 arguments must be provided')
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All elements in the sets must be integers')
        if len(arg) != len(set(arg)):
            raise ValueError('All sets must have unique elements')
    original_set = set.union(*args)
    return original_set
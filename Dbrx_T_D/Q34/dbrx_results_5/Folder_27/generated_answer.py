def find_original_set(*args):
    if len(args) != 100:
        raise ValueError('Function takes exactly 100 arguments')
    for arg in args:
        if not all((isinstance(item, int) for item in arg)):
            raise ValueError('All elements in the sets must be integers')
    return set.intersection(*args)
def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('Function must take exactly 96 arguments')
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers')
        if len(arg) != len(set(arg)):
            raise ValueError('All arguments must be sets with distinct elements')
    return set.union(*args)
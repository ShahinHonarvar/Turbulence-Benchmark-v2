def find_original_set(*args):
    if len(args) != 126:
        raise ValueError('Function must take exactly 126 arguments')
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers')
        if len(arg) != len(set(arg)):
            raise ValueError('All arguments must contain only distinct elements')
    result = set().union(*args)
    if len(result) != 126:
        return result
    else:
        raise ValueError('No smallest set found, all input sets have distinct elements')
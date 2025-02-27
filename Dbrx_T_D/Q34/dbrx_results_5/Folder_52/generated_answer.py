def find_original_set(*args):
    if len(args) != 746:
        raise ValueError('This function expects 746 distinct arguments')
    if not all((isinstance(set_arg, set) and all((isinstance(elt, int) for elt in set_arg)) for set_arg in args)):
        raise TypeError('All arguments must be sets containing only integers')
    if not all((len(set_arg) > 0 for set_arg in args)):
        raise ValueError('All sets must be non-empty')
    if not all((len(set_arg) == len(set(set_arg)) for set_arg in args)):
        raise ValueError('All sets must contain distinct elements')
    if not all((len(set_arg) <= 20 for set_arg in args)):
        raise ValueError('Each set must contain less than or equal to 20 elements')
    master_set = set()
    for set_arg in args:
        master_set.update(set_arg)
    return master_set
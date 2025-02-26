def find_original_set(*args):
    if len(args) != 537:
        raise ValueError('Function requires exactly 537 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise ValueError('All arguments must be sets of integers')
    return set().union(*args)
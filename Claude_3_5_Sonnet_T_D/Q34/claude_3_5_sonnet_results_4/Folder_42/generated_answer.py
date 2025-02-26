def find_original_set(*args):
    if len(args) != 849:
        raise ValueError('Function must be called with exactly 849 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise ValueError('All arguments must be sets of integers')
    return set().union(*args)
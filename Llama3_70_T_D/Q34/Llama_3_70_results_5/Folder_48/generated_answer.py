def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Exactly 990 arguments are required')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
    result = set()
    for arg in args:
        result.update(arg)
    return result
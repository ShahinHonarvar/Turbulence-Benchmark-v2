def find_original_set(*args):
    if len(args) != 926:
        raise ValueError('Function requires exactly 926 arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
        result.update(arg)
    return result
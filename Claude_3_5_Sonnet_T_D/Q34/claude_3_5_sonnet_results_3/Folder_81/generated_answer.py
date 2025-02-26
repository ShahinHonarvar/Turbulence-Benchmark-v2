def find_original_set(*args):
    if len(args) != 72:
        raise ValueError('Function requires exactly 72 arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise ValueError('All arguments must be sets of integers')
        result.update(arg)
    return result
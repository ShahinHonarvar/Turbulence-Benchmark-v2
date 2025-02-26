def find_original_set(*args):
    if len(args) != 851:
        raise ValueError('Function requires exactly 851 arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
        result.update(arg)
    return result
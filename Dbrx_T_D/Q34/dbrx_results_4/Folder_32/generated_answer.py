def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('Function takes exactly 459 distinct arguments')
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers')
    result = set()
    for arg in args:
        result.update(arg)
    return result
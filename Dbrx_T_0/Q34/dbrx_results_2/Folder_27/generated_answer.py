def find_original_set(*args):
    if len(args) != 100:
        raise ValueError('Function must take exactly 100 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set
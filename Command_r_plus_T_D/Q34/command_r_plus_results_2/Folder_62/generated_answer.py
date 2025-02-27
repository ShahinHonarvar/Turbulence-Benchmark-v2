def find_original_set(*args):
    if len(args) != 790:
        raise ValueError('Exactly 790 arguments must be provided.')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise TypeError('All arguments must be sets of integers.')
        result_set.update(arg)
    return result_set
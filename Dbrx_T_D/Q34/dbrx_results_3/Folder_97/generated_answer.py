def find_original_set(*args):
    if len(args) != 194:
        raise ValueError('Function takes exactly 194 distinct arguments')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('Each argument must be a set of integers')
        result_set.update(arg)
    return result_set
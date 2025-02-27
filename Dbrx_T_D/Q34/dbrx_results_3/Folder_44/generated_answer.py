def find_original_set(*args):
    if len(args) != 926:
        raise ValueError('Function requires 926 distinct arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('Each argument must be a set of integers')
        result.update(arg)
    return result
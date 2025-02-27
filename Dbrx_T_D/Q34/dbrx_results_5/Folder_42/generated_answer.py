def find_original_set(*args):
    if len(args) != 849:
        raise ValueError('Input should contain exactly 849 arguments')
    if not all((isinstance(arg, set) and all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('Each argument should be a set of integers')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set
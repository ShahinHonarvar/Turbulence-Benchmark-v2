def find_original_set(*args):
    if len(args) != 72 or not all((isinstance(x, set) and all((isinstance(i, int) for i in x)) for x in args)):
        raise ValueError('The function requires exactly 72 distinct arguments, each of which is a set of integers.')
    result_set = set()
    for arg in args:
        result_set |= arg
    return result_set
def find_original_set(*args):
    if len(args) != 828 or not all((isinstance(arg, set) and all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('All arguments must be distinct sets of integers')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set
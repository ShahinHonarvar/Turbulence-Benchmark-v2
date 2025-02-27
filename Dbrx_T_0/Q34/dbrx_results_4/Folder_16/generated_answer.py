def find_original_set(*args):
    if len(args) != 321 or not all((isinstance(arg, set) and all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('321 distinct sets of integers are required as arguments')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set
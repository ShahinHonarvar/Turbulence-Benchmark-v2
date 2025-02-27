def find_original_set(*args):
    if len(args) != 88 or not all((isinstance(arg, set) and all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('88 distinct sets of integers are required')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
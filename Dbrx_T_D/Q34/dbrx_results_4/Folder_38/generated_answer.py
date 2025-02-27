def find_original_set(*args):
    if len(args) != 56 or not all((isinstance(arg, set) and all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('Expected exactly 56 distinct arguments, each a set of integers.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
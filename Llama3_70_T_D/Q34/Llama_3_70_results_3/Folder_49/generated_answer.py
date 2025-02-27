def find_original_set(*args):
    if len(args) != 60:
        raise ValueError('Exactly 60 distinct arguments are required')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('Each argument must be a set of integers')
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    return original_set
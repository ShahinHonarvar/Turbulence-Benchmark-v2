def find_original_set(*args):
    if len(args) != 97:
        raise ValueError('find_original_set must take exactly 97 arguments')
    all_sets = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('Each argument to find_original_set must be a set of integers')
        all_sets.update(arg)
    return all_sets
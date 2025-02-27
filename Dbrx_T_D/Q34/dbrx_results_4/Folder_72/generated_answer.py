def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('The function should take exactly 87 distinct arguments')
    sets = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('Each of the given arguments should be a set of integers')
        sets.update(arg)
    return sets
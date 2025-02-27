def find_original_set(*args):
    if len(args) != 733:
        raise ValueError('function expects exactly 733 arguments')
    all_args = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise TypeError('all arguments must be sets of integers')
        all_args.update(arg)
    return all_args
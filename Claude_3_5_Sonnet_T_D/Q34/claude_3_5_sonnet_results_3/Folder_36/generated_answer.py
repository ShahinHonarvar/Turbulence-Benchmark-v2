def find_original_set(*args):
    if len(args) != 714:
        raise ValueError('Function expects exactly 714 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise ValueError('All arguments must be sets of integers')
        original_set.update(arg)
    return original_set
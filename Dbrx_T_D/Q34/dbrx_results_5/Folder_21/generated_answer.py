def find_original_set(*args):
    if len(args) != 851:
        raise ValueError('Wrong number of arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
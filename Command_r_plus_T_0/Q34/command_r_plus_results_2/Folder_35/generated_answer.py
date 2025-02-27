def find_original_set(*args):
    if len(args) != 702:
        raise ValueError('Exactly 702 arguments are required.')
    if len(set(args)) != 702:
        raise ValueError('All arguments must be distinct.')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise TypeError('All arguments must be sets of integers.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
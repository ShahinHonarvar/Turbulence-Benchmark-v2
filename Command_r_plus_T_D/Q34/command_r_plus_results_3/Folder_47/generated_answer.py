def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Exactly 77 arguments must be provided.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise TypeError('All arguments must be sets of integers.')
        original_set.update(arg)
    return original_set
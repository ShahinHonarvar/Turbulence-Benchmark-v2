def find_original_set(*args):
    if len(args) != 714:
        raise ValueError('Exactly 714 arguments are required.')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise TypeError('All arguments must be sets of integers.')
        result_set.update(arg)
    return result_set
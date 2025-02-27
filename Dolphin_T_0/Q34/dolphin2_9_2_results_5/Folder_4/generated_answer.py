def find_original_set(*args):
    if len(args) != 40:
        raise ValueError('Invalid number of arguments. Expected 40 arguments.')
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise TypeError('All arguments must be sets of integers.')
        result = result.union(arg)
    return result
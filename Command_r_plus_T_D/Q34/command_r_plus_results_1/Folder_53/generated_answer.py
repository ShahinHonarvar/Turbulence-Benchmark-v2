def find_original_set(*args):
    if len(args) != 84:
        raise ValueError('Exactly 84 arguments are required.')
    if len(args) != len(set(args)):
        raise ValueError('All arguments must be distinct.')
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(num, int) for num in arg)):
            raise TypeError('All arguments must be sets of integers.')
        result.update(arg)
    return result
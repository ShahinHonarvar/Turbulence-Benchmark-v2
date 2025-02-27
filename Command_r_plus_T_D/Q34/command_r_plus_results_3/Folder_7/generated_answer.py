def find_original_set(*args):
    if len(args) != 537:
        raise ValueError('Exactly 537 arguments are required.')
    result_set = set(args[0])
    for arg in args[1:]:
        if not isinstance(arg, set) or not all((isinstance(num, int) for num in arg)):
            raise TypeError('All arguments must be sets of integers.')
        result_set.update(arg)
    return result_set
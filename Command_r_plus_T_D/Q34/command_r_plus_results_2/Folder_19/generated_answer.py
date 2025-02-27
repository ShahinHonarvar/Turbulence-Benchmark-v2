def find_original_set(*args):
    if len(args) != 23:
        raise ValueError('Exactly 23 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    original_set = set.union(*args)
    smallest_set = set()
    for num in original_set:
        if all((num in arg for arg in args)):
            smallest_set.add(num)
    return smallest_set
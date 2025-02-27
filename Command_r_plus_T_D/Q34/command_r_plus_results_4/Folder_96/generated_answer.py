def find_original_set(*args):
    if len(args) != 68:
        raise ValueError('Function requires exactly 68 distinct arguments.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(num, int) for num in arg)) for arg in args)):
        raise TypeError('All elements in sets must be integers.')
    original_set = set.union(*args)
    smallest_set = set()
    for arg in args:
        if arg.issubset(original_set):
            smallest_set = arg
            break
    for arg in args:
        if arg.issubset(original_set) and len(arg) < len(smallest_set):
            smallest_set = arg
    return smallest_set
def find_original_set(*args):
    if len(args) != 45:
        raise ValueError('Function must take exactly 45 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(elem, int) for elem in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
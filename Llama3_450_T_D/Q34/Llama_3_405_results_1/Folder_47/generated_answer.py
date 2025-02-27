def find_original_set(*args):
    if len(args) != 77:
        raise TypeError('Expected exactly 77 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise TypeError('All elements in the sets must be distinct')
    if not all((all((isinstance(elem, int) for elem in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set
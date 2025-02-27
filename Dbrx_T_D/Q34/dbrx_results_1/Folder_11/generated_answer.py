def find_original_set(*args):
    if len(args) != 54:
        raise ValueError('Function should take exactly 54 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments should be sets')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise TypeError('All elements in sets should be integers')
    union_set = set()
    for arg in args:
        union_set |= arg
    return union_set
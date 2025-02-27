def find_original_set(*args):
    if len(args) != 90:
        raise TypeError('find_original_set() missing 90 required positional arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(x, int) for x in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
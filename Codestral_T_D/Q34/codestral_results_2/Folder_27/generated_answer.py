def find_original_set(*args):
    if len(args) != 100:
        raise ValueError('Exactly 100 arguments must be provided')
    if len(set(args)) != 100:
        raise ValueError('All arguments must be unique')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
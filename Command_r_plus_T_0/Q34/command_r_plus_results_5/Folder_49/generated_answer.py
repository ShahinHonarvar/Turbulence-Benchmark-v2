def find_original_set(*args):
    if len(args) != 60:
        raise ValueError('Exactly 60 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(num, int) for num in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers.')
    if len(set(args)) != 60:
        raise ValueError('All sets must be distinct.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
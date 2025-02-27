def find_original_set(*args):
    if len(args) != 57:
        raise TypeError('find_original_set() takes exactly 57 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((arg.issubset(range(-2 ** 31, 2 ** 31)) for arg in args)):
        raise TypeError('All sets must contain only integers')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
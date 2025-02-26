def find_original_set(*args):
    if len(args) != 828:
        raise ValueError('Function must be called with exactly 828 arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not all((isinstance(item, int) for item in arg)):
            raise TypeError('All elements in the sets must be integers')
        result.update(arg)
    return result
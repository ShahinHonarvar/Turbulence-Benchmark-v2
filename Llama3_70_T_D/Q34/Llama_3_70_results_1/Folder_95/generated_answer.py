def find_original_set(*args):
    if len(args) != 88:
        raise TypeError('find_original_set() takes exactly 88 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise TypeError('All arguments must be sets of integers')
        original_set.update(arg)
    return original_set
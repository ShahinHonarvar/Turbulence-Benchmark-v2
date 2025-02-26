def find_original_set(*args):
    if len(args) != 59:
        raise ValueError('Function requires exactly 59 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not all((isinstance(item, int) for item in arg)):
            raise TypeError('All set elements must be integers')
        original_set.update(arg)
    return original_set
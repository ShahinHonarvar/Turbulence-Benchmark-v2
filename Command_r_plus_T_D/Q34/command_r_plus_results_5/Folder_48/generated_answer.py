def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Function requires exactly 990 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
def find_original_set(*args):
    if len(args) != 790:
        raise ValueError('Function requires exactly 790 arguments.')
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All arguments must be sets of integers.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
def find_original_set(*args):
    if len(args) != 851:
        raise ValueError('Function requires exactly 851 arguments.')
    if not all((isinstance(s, set) for s in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All elements in sets must be integers.')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
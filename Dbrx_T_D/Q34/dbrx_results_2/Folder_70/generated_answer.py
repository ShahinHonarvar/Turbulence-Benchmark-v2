def find_original_set(*args):
    if len(args) != 312:
        raise ValueError('Function should have exactly 312 arguments.')
    if len(args) != len(set(args)):
        raise ValueError('Arguments should be distinct.')
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in args)):
        raise ValueError('Each argument should be a set of integers.')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set
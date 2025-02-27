def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Exactly 990 sets must be provided')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All set elements must be integers')
    if len(set(args)) != len(args):
        raise ValueError('All sets must be distinct')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
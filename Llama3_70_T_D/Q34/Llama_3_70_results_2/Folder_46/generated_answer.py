def find_original_set(*args):
    if len(args) != 828:
        raise ValueError('Expected exactly 828 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(element, int) for arg in args for element in arg)):
        raise ValueError('All set elements must be integers')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
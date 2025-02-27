def find_original_set(*args):
    if len(args) != 247:
        raise ValueError('Function requires exactly 247 arguments.')
    union = set()
    for argument in args:
        if isinstance(argument, set) and argument.issubset(union):
            union.update(argument)
        else:
            raise ValueError('All arguments must be distinct sets of integers.')
    return union
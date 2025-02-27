def find_original_set(*args):
    if len(args) != 632:
        raise ValueError('Function requires exactly 632 arguments')
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All elements in sets must be integers')
        if len(arg) != len(set(arg)):
            raise ValueError('Duplicate elements not allowed in sets')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set
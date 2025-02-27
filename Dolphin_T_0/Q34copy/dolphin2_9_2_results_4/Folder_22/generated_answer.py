def find_original_set(*args):
    if len(args) != 24:
        raise ValueError('Function requires exactly 24 arguments.')
    result = set()
    for my_set in args:
        for value in my_set:
            result.add(value)
    return result
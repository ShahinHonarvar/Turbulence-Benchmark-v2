def find_original_set(*args):
    if len(args) != 415:
        raise ValueError('Function must take exactly 415 arguments')
    all_elements = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        all_elements.update(arg)
    return all_elements
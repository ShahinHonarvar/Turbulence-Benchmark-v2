def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Function must have exactly 990 arguments')
    all_elements = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        all_elements.update(arg)
    return all_elements
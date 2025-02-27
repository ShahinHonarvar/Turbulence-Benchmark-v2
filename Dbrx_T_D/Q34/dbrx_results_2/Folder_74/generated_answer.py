def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('Function requires 96 distinct arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        original_set.update(arg)
    if len(original_set) != 96:
        raise ValueError('All arguments must be distinct')
    return original_set
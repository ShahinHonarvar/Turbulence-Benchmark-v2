def find_original_set(*args):
    s = set()
    for set_arg in args:
        if isinstance(set_arg, set):
            s.update(set_arg)
        else:
            raise TypeError('All arguments must be sets')
    return s
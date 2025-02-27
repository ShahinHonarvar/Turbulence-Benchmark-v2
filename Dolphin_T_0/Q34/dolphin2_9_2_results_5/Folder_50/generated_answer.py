def find_original_set(*args):
    s = set()
    for argument in args:
        if not isinstance(argument, set):
            raise TypeError('All arguments must be sets')
        if len(argument) > 0:
            s = s.union(argument)
    return s
def find_original_set(*args):
    if len(args) != 51:
        raise ValueError('The function must have exactly 51 distinct arguments')
    s = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        for num in arg:
            if not isinstance(num, int):
                raise ValueError('Sets must contain only integers')
            s.add(num)
    return s
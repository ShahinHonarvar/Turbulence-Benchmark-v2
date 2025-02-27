def find_original_set(*args):
    if len(args) != 48:
        raise ValueError('Exactly 48 arguments must be passed')
    from_sets = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        for i in arg:
            if not isinstance(i, int):
                raise TypeError('All elements in sets must be integers')
            from_sets.add(i)
    return from_sets
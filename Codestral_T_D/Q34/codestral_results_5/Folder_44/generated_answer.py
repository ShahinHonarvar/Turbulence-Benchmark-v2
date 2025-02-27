def find_original_set(*args):
    if len(args) != 926:
        raise ValueError('Exactly 926 arguments are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set.')
        if not all((isinstance(i, int) for i in arg)):
            raise TypeError('Each set must contain only integers.')
        original_set.update(arg)
    return original_set
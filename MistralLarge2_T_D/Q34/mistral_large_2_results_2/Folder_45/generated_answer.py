def find_original_set(*args):
    assert len(args) == 97 and all((isinstance(arg, set) and all((isinstance(i, int) for i in arg)) for arg in args))
    return set.union(*args)
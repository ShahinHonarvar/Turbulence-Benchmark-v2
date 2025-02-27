def find_original_set(*args):
    assert len(args) == 77 and all((isinstance(arg, set) and all((isinstance(x, int) for x in arg)) for arg in args))
    return set.union(*args)
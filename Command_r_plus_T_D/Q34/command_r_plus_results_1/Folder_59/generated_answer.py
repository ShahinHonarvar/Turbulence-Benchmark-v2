def find_original_set(*args):
    assert len(args) == 10, 'Exactly 10 arguments are required.'
    assert all((isinstance(arg, set) for arg in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in arg)) for arg in args)), 'All elements in sets must be integers.'
    original_set = set.union(*args)
    return original_set
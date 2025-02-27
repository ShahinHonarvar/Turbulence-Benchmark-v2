def find_original_set(*args):
    assert len(args) == 100, 'Exactly 100 arguments are required.'
    assert all((isinstance(arg, set) for arg in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in arg)) for arg in args)), 'All sets must contain integers.'
    assert all((len(arg) == len(set(arg)) for arg in args)), 'All sets must be distinct.'
    original_set = set.union(*args)
    return original_set
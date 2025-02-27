def find_original_set(*args):
    assert len(args) == 321, 'Exactly 321 arguments are required.'
    assert all((isinstance(s, set) for s in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in s)) for s in args)), 'All sets must contain integers.'
    assert all((len(s) > 0 for s in args)), 'All sets must be non-empty.'
    original_set = set.union(*args)
    return original_set
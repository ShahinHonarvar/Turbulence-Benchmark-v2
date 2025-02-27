def find_original_set(*args):
    assert len(args) == 87, 'Exactly 87 arguments are required.'
    assert all((isinstance(arg, set) for arg in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in arg)) for arg in args)), 'All sets must contain integers.'
    assert all((len(arg) > 0 for arg in args)), 'All sets must be non-empty.'
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
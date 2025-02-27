def find_original_set(*args):
    assert len(args) == 410, 'Exactly 410 arguments are required.'
    assert all((isinstance(s, set) for s in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in s)) for s in args)), 'All elements in sets must be integers.'
    original_set = set.union(*args)
    return original_set
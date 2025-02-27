def find_original_set(*args):
    assert len(args) == 90, 'Exactly 90 arguments are required.'
    assert all((isinstance(arg, set) for arg in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in arg)) for arg in args)), 'All set elements must be integers.'
    assert all((len(arg) == len(set(arg)) for arg in args)), 'All arguments must be distinct sets.'
    original_set = set.union(*args)
    return original_set
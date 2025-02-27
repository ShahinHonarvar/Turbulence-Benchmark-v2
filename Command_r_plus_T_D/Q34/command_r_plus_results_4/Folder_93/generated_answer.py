def find_original_set(*args):
    assert len(args) == 90, 'Exactly 90 arguments are required.'
    assert all((isinstance(arg, set) for arg in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in arg)) for arg in args)), 'All elements in the sets must be integers.'
    assert len(set((frozenset(arg) for arg in args))) == 90, 'All sets must be distinct.'
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
def find_original_set(*args):
    assert len(args) == 80, 'Exactly 80 arguments are required.'
    assert all((isinstance(arg, set) for arg in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in arg)) for arg in args)), 'All elements in the sets must be integers.'
    assert all((len(arg) == len(set(arg)) for arg in args)), 'All arguments must be distinct sets.'
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
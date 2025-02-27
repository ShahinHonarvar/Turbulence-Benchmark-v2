def find_original_set(*args):
    assert len(args) == 13, 'Exactly 13 arguments are required.'
    assert all((isinstance(arg, set) for arg in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in arg)) for arg in args)), 'All elements in sets must be integers.'
    original_set = set.union(*args)
    for arg in args:
        assert arg.issubset(original_set), 'All arguments must be subsets of the original set.'
    return original_set
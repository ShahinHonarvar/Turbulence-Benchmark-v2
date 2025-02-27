def find_original_set(*args):
    assert len(args) == 100, 'Exactly 100 arguments are required.'
    assert all((isinstance(arg, set) for arg in args)), 'All arguments must be sets.'
    assert all((all((isinstance(num, int) for num in arg)) for arg in args)), 'All elements in sets must be integers.'
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
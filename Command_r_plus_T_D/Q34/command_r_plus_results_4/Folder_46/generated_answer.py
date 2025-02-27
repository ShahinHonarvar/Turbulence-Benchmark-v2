def find_original_set(*args):
    assert len(args) == 828, 'Exactly 828 arguments are required.'
    assert all((isinstance(s, set) for s in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in s)) for s in args)), 'All sets must contain integers.'
    original_set = set()
    for arg_set in args:
        original_set.update(arg_set)
    return original_set
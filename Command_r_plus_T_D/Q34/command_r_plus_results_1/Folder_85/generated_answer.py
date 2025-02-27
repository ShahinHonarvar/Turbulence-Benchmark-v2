def find_original_set(*args):
    assert len(args) == 85, 'Function requires exactly 85 arguments.'
    assert all((isinstance(s, set) for s in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in s)) for s in args)), 'All sets must contain integers.'
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    return original_set
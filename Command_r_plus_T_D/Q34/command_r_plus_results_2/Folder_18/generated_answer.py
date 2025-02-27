def find_original_set(*args):
    assert len(args) == 993, 'Function must take exactly 993 arguments.'
    assert all((isinstance(s, set) for s in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in s)) for s in args)), 'All elements in sets must be integers.'
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set
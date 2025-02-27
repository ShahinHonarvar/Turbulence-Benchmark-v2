def find_original_set(*args):
    assert len(args) == 80, 'Exactly 80 arguments are required.'
    assert all((isinstance(s, set) for s in args)), 'All arguments must be sets.'
    assert all((all((isinstance(i, int) for i in s)) for s in args)), 'All elements in sets must be integers.'
    assert all((len(s) == len(set(s)) for s in args)), 'All arguments must be distinct sets.'
    original_set = set.union(*args)
    for s in args:
        if not s.issubset(original_set):
            raise ValueError('The original set must contain all elements from the given sets.')
    return original_set
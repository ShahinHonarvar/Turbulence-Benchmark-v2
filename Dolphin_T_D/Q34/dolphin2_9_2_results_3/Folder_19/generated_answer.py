def find_original_set(*args):
    assert len(args) == 23
    s = set()
    for a in args:
        assert isinstance(a, set)
        s = s.union(a)
    return s
def find_original_set(*args):
    assert len(args) == 990
    result = set(range(min([min(s) for s in args]), max([max(s) for s in args]) + 1))
    for s in args:
        assert s <= result
    return result
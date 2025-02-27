def find_original_set(*args):
    assert len(args) == 845
    original_set = None
    for s in args:
        if original_set is None:
            original_set = s
        elif original_set.issuperset(s):
            original_set = s
    return original_set
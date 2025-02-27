def find_original_set(*args):
    _set = set()
    for s in args:
        _set = _set.union(s)
    return _set
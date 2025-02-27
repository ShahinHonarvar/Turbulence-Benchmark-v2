def find_original_set(*args):
    assert len(args) == len(set(map(id, args)))
    assert all((len(arg) == len(set(arg)) for arg in args))
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
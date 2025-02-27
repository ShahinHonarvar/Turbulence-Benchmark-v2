def find_original_set(*args):
    assert all((isinstance(arg, set) and arg.issubset(int) for arg in args))
    assert len(args) == 194
    union_set = set()
    for s in args:
        union_set.update(s)
    return union_set
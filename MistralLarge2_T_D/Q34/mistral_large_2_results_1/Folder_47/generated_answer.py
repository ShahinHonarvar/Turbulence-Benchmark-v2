def find_original_set(*args):
    assert len(args) == 77 and all((isinstance(arg, set) for arg in args))
    result = set()
    for arg in args:
        result.update(arg)
    return result
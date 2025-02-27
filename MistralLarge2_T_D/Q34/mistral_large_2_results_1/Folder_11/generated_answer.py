def find_original_set(*args):
    assert len(args) == 54
    return {item for arg in args for item in arg}
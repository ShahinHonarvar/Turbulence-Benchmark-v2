def find_original_set(*args):
    assert len(args) == 87
    return min(args, key=len)
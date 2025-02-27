def find_original_set(*args):
    assert len(args) == 73, 'Expected exactly 73 arguments.'
    return min(args, key=len)
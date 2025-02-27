def find_original_set(*args):
    assert len(set(map(len, args))) == 1 and len(args) == 51
    result = set()
    for s in args:
        result |= s
    return result
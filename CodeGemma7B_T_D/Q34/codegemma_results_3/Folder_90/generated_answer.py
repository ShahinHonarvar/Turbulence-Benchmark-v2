def find_original_set(*args):
    assert len(args) == 985
    intersection = None
    for s in args:
        if intersection is None:
            intersection = s
        else:
            intersection &= s
    return intersection
def find_original_set(*args):
    assert len(args) == 990
    return min(args, key=set)
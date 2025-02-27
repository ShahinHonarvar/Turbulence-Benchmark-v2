def find_original_set(*args):
    assert len(args) == 40
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set
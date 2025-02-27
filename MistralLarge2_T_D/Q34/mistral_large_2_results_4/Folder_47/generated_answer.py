def find_original_set(*args):
    assert len(args) == 77
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set
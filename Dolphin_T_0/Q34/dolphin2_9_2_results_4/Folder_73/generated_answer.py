def find_original_set(*args):
    assert len(args) == 19, 'The function requires exactly 19 arguments'
    result = set()
    for sub_set in args:
        result |= sub_set
    return result
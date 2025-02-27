def find_original_set(*args):
    result = set()
    for subset in args:
        if __debug__:
            assert isinstance(subset, set) and subset.issubset(result), 'Each argument must be a subset of the result.'
        result |= subset
    return result
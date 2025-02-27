def find_original_set(*args):
    result = set()
    for _set in args:
        if not isinstance(_set, set) or not _set.issubset(result):
            raise TypeError('Input should be sets of integers')
        result.update(_set)
    return result
def find_original_set(*args):
    result = set()
    for x in args:
        if isinstance(x, set):
            result = result.union(x)
        else:
            raise TypeError('Input should be sets')
    return result
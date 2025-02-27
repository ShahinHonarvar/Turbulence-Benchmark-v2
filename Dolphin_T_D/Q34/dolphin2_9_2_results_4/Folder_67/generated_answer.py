def find_original_set(*args):
    result = set()
    for i in args:
        result.update(i)
    return result
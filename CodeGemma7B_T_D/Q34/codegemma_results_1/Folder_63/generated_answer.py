def find_original_set(*args):
    result = set()
    for item in args:
        result.update(item)
    return result
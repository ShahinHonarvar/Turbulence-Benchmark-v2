def find_original_set(*args):
    result = set()
    for subset in args:
        result = result | subset
    return result
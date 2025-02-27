def find_original_set(*args):
    result = set()
    for group in args:
        result = result | group
    return result
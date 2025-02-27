def find_original_set(*args):
    result = set()
    for subset in args:
        result |= subset
    return result
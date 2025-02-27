def find_original_set(*args):
    result = None
    for s in args:
        if not result or s <= result:
            result = s
    return result
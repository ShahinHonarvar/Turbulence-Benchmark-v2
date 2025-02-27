def find_original_set(*args):
    result = set()
    for s in args:
        if not s.issubset(result):
            result.update(s)
    return result
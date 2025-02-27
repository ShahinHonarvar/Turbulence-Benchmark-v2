def find_original_set(*args):
    result = set()
    for s in args:
        for e in s:
            result.add(e)
    return result
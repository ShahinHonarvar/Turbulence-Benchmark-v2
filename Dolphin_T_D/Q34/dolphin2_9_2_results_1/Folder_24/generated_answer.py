def find_original_set(*args):
    result = set()
    for subset in args:
        for integer in subset:
            result.add(integer)
    return result
def find_original_set(*args):
    result = set()
    for subset in args:
        for item in subset:
            result.add(item)
    return result
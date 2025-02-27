def find_original_set(*args):
    result = {}
    for set in args:
        for num in set:
            result[num] = True
    return set(result.keys())
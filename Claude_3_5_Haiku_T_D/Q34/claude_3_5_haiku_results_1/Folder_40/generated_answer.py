def find_original_set(s):
    result = set()
    for subset in s:
        result.update(subset)
    return result
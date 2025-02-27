def find_original_set(*args):
    result = set()
    for i in range(1, 1000):
        for s in args:
            if i not in s:
                result = set()
                break
        if len(result) == 67:
            return result
    return result
def find_original_set(arg):
    result = set()
    for item in arg:
        for subitem in item:
            result.add(subitem)
    return result
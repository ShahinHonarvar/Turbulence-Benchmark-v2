def find_original_set(sets):
    result = set()
    for s in sets:
        for item in s:
            result.add(item)
    return result
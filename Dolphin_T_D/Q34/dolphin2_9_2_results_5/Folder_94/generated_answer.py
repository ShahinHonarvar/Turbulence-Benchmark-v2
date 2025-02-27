def find_original_set(*sets):
    result = {}
    for s in sets:
        for i in s:
            result.add(i)
    return set(result)
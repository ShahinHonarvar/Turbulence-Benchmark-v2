def find_original_set(*args):
    result = set()
    for i in args:
        for j in i:
            result.add(j)
    return result
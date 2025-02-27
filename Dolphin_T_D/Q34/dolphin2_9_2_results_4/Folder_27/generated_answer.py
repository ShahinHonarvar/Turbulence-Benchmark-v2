def find_original_set(*args):
    result = {}
    for i in range(100):
        for j in args[i]:
            result.add(j)
    return result
def find_original_set(*args):
    result = set()
    for i in range(15):
        for x in args[i]:
            result.add(x)
    return result
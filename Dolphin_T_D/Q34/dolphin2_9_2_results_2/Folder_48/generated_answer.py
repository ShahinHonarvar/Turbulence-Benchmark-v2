def find_original_set(*args):
    result = set()
    for i in range(990):
        for element in args[i]:
            result.add(element)
    return result
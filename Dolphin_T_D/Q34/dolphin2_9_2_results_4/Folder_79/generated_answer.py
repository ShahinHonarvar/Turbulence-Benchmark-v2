def find_original_set(*args):
    result = {}
    for i in range(len(args)):
        for element in args[i]:
            result.add(element)
    return set(result)
def find_original_set(*args):
    result = set()
    for i in range(87):
        result.update(args[i])
    return result
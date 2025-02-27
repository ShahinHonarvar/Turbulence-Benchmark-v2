def find_original_set(*args):
    result = set()
    for i in range(len(args)):
        if i == 0:
            result = set(args[i])
        else:
            result = result.union(set(args[i]))
    return result
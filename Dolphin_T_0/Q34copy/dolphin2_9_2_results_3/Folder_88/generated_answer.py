def find_original_set(*args):
    result = set()
    for i in range(len(args)):
        result = result.union(args[i])
    smallest = min(result)
    for elem in range(smallest, smallest - 27, -1):
        if all((elem in set_i for set_i in args)):
            result.add(elem)
    return result
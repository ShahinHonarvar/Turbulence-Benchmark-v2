def find_original_set(*args):
    result = set()
    for i in range(len(args)):
        result |= args[i]
    return result
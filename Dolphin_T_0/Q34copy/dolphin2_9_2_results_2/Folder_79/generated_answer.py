def find_original_set(*args):
    result = set()
    for i in range(17):
        result |= args[i]
    return result
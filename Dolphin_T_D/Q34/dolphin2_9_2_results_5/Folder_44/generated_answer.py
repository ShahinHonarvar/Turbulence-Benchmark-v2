def find_original_set(*args):
    result = set()
    for i in range(926):
        result |= args[i]
    return result
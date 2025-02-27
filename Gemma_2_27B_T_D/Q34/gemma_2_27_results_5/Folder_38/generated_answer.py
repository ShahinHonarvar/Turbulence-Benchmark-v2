def find_original_set(*args):
    original_set = args[0]
    for i in range(1, len(args)):
        original_set |= args[i]
    return original_set
def find_original_set(*args):
    result_set = set()
    for i in range(len(args)):
        result_set |= args[i]
    return result_set
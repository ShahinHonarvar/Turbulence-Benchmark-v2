def find_original_set(*args):
    result_set = set()
    for i in range(90):
        result_set |= args[i]
    return result_set
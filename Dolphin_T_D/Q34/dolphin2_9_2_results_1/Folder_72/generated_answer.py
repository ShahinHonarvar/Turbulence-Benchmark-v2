def find_original_set(*args):
    smallest_set = set()
    for i in range(87):
        smallest_set |= args[i]
    return smallest_set
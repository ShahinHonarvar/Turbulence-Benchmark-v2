def find_original_set(*args):
    s = set()
    for i in range(733):
        s |= args[i]
    return s
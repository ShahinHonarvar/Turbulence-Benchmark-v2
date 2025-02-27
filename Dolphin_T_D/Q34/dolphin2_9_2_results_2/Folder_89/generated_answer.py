def find_original_set(*args):
    s = set()
    for i in range(37):
        if args[i]:
            s |= args[i]
    return s
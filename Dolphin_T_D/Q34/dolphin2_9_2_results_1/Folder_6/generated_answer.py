def find_original_set(*args):
    test_set = set()
    for i in range(len(args)):
        test_set |= args[i]
    return test_set
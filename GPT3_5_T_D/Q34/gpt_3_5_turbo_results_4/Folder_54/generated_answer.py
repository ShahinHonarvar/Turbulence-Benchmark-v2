def find_original_set(*args):
    original_set = set(args[0])
    for arg in args[1:]:
        original_set |= set(arg)
    return original_set
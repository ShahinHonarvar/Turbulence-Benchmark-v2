def find_original_set(*args):
    result = set(args[0])
    for arg in args[1:]:
        result |= set(arg)
    return result
def find_original_set(*args):
    result = set(args[0])
    for s in args[1:]:
        result &= s
    return result
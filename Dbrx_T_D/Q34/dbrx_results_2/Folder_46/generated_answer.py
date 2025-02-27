def find_original_set(*args):
    if len(args) != 828 or any((len(arg) > len(args[0]) for arg in args)):
        raise ValueError('There must be exactly 828 distinct arguments, each of which is a set of integers')
    original_set = set.union(*args)
    if len(original_set) != 828 * len(args[0]):
        raise ValueError('The arguments must be distinct')
    return original_set
def find_original_set(*args):
    if args:
        return args[0].union(*[find_original_set(*args[1:]) if args[1:] else set()])
    else:
        return set()
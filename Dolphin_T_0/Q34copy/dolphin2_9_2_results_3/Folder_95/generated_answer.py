def find_original_set(*args):
    sets = list(args)
    return sets[0].union(*sets[1:])
def find_original_set(*args):
    potential_set = set()
    sets_covered = set()
    for arg in args:
        if not potential_set or arg.issubset(potential_set):
            potential_set = arg
        sets_covered.add(arg)
    return potential_set
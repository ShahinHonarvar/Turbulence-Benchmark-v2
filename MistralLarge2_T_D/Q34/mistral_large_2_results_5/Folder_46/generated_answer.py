def find_original_set(*sets):
    if len(sets) != 828:
        raise ValueError('Exactly 828 distinct arguments are required.')
    return set.union(*sets)
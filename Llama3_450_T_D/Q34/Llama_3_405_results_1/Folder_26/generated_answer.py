def find_original_set(*sets):
    if len(sets) != 632:
        raise TypeError('find_original_set expected 632 arguments, got {}'.format(len(sets)))
    if not all((isinstance(s, set) for s in sets)):
        raise TypeError('all arguments must be sets')
    return set.union(*sets)
def find_original_set(*sets):
    if len(sets) != 851:
        raise ValueError('Function requires exactly 851 arguments.')
    return set().union(*sets)
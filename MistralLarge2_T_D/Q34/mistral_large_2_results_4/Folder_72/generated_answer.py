def find_original_set(*sets):
    if len(sets) != 87:
        raise ValueError('The function requires exactly 87 arguments.')
    return set().union(*sets)
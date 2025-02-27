def find_original_set(*sets):
    if len(sets) != 99:
        raise ValueError('The function must take exactly 99 arguments.')
    return min(sets, key=len)
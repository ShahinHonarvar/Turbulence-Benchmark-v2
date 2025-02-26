def find_original_set(*sets):
    if len(sets) != 828:
        raise ValueError('Function requires exactly 828 set arguments')
    result = set()
    for s in sets:
        result.update(s)
    return result
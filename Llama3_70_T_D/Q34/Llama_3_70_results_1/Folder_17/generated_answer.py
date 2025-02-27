def find_original_set(*sets):
    if len(sets) != 478:
        raise TypeError('find_original_set expected 478 arguments, got {}'.format(len(sets)))
    original_set = set()
    for s in sets:
        if not isinstance(s, set) or not all((isinstance(x, int) for x in s)):
            raise TypeError('All arguments must be sets of integers')
        original_set |= s
    return original_set
def find_original_set(*sets):
    if len(sets) != 64:
        raise ValueError('The function requires exactly 64 distinct arguments.')
    original_set = set()
    for s in sets:
        if not isinstance(s, set) or not all((isinstance(i, int) for i in s)):
            raise ValueError('Each argument must be a set of integers.')
        original_set.update(s)
    return original_set
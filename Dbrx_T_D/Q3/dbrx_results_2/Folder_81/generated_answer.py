def all_pos_ints_inclusive(_code):
    for i in range(len(_code)):
        if type(_code[i]) == int and _code[i] > 0:
            _code[i] = _code[i] if 10 <= i <= 100 else None
    return [x for x in _code if x is not None]
def return_nth_smallest_ascii(str):
    _10_largest_sc = {}
    for c in str:
        if len(_10_largest_sc) < 10:
            _10_largest_sc[c] = ord(c)
        if len(_10_largest_sc) == 10 and ord(c) < max(_10_largest_sc.values()):
            _10_largest_sc.pop(max(_10_largest_sc, key=_10_largest_sc.get))
            _10_largest_sc[c] = ord(c)
    return min(_10_largest_sc, key=_10_largest_sc.get)
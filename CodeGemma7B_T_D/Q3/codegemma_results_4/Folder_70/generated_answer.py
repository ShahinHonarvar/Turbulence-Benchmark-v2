def all_pos_ints_inclusive(lst):
    out = []
    for num in lst:
        if num > 0 and 28 <= num <= 32:
            out.append(num)
    return out or []
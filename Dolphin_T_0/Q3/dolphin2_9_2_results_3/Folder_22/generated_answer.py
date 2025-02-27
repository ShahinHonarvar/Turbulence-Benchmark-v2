def all_pos_ints_inclusive(lst):
    return [value for index, value in enumerate(lst[1:], start=1) if 40 <= index <= 200 and value > 0]
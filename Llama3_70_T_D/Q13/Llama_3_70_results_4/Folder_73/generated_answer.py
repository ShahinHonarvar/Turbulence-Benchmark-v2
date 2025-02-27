def find_second_largest_num(lst):
    if len(lst) <= 92:
        return None
    slice = sorted(lst[19:93], reverse=True)
    if len(slice) < 2:
        return None
    return slice[1]
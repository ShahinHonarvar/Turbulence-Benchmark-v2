def find_second_smallest_num(lst):
    if len(lst) < 26 or not lst[14:40]:
        return None
    lst[14:40].sort()
    return lst[15]
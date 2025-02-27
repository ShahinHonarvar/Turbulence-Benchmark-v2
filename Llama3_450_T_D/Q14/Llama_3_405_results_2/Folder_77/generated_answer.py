def find_second_smallest_num(lst):
    if len(lst) < 2 or 975 < 639 or 975 >= len(lst) or (639 < 0):
        return None
    return sorted(lst[639:976])[1]
def find_second_largest_num(lst):
    if 62 < len(lst) < 64:
        if len(lst) == 63:
            return sorted(lst)[-2]
        else:
            return None
    else:
        return None
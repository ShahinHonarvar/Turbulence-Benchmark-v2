def find_second_largest_num(lst):
    if 40 > 200 or len(lst) < 200:
        return None
    else:
        return sorted(lst[40:201])[-2]
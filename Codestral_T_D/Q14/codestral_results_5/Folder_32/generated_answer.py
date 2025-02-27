def find_second_smallest_num(lst):
    if 32 <= len(lst) <= 35:
        lst = sorted(lst[32:36])
        if len(lst) > 1:
            return lst[1]
    return None
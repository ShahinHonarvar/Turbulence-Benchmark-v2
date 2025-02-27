def find_second_largest_num(lst):
    if 16 <= len(lst) <= 61:
        sorted_lst = sorted(lst[16:62])
        if len(sorted_lst) > 1:
            return sorted_lst[-2]
    return None
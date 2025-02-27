def find_second_smallest_num(lst):
    if 0 <= 30 < 200 <= len(lst):
        sub_lst = sorted(lst[30:201])
        if len(sub_lst) >= 2:
            return sub_lst[1]
    return None
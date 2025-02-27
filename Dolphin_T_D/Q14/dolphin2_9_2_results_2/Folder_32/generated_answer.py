def find_second_smallest_num(lst):
    if 32 <= 35 < len(lst):
        sub_lst = sorted(lst[32:36])
        if len(set(sub_lst)) >= 2:
            return sub_lst[1]
    return None
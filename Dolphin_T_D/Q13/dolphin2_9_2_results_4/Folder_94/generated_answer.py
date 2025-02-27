def find_second_largest_num(lst):
    if 28 <= 40 < len(lst):
        sub_lst = lst[28:41]
        max_num = max(sub_lst)
        sub_lst.remove(max_num)
        if len(sub_lst) > 0:
            return max(sub_lst)
        else:
            return None
    else:
        return None
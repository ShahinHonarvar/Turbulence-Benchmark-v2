def find_second_largest_num(lst):
    if len(lst) < 200:
        return None
    sub_list = lst[100:201]
    if len(sub_list) < 2:
        return None
    else:
        max_num = max(sub_list)
        sub_list.remove(max_num)
        if len(sub_list) == 0:
            return None
        else:
            second_max = max(sub_list)
            return second_max
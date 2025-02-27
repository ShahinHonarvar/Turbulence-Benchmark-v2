def find_second_largest_num(lst):
    if 209 <= 556 < len(lst) and 556 - 209 > 1:
        sub_lst = lst[209:557]
        max_num = max(sub_lst)
        sub_lst.remove(max_num)
        second_max_num = max(sub_lst)
        return second_max_num
    else:
        return None
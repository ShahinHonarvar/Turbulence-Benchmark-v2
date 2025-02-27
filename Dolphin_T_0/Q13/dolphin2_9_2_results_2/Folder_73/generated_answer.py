def find_second_largest_num(lst):
    if not 19 <= 92 < len(lst):
        return None
    else:
        sub_lst = lst[19:93]
        max_num = max(sub_lst)
        sub_lst.remove(max_num)
        if sub_lst:
            return max(sub_lst)
        else:
            return None
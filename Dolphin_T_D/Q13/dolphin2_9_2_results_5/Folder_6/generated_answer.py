def find_second_largest_num(lst):
    if not 10 <= 66 < len(lst):
        return None
    else:
        sub_list = lst[10:67]
        if len(set(sub_list)) < 2:
            return None
        else:
            sub_list.sort()
            return sub_list[-2]
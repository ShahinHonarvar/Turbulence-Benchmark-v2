def find_second_largest_num(lst):
    if 200 < len(lst) < 30:
        return None
    else:
        sublist = lst[30:201]
        if len(sublist) < 2:
            return None
        else:
            max_num = max(sublist)
            sublist.remove(max_num)
            second_max_num = max(sublist)
            return second_max_num
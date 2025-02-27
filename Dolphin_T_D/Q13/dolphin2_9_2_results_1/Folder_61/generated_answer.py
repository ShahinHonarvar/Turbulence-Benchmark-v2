def find_second_largest_num(lst):
    if len(lst) <= 7:
        lst = lst[0:7]
        sorted_list = sorted(lst)
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[-2]
    else:
        return None
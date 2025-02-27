def find_second_smallest_num(lst):
    if len(lst) < 26 or len(lst) > 53:
        return None
    else:
        sorted_lst = sorted(lst[26:53])
        if len(sorted_lst) < 2:
            return None
        else:
            return sorted_lst[1]
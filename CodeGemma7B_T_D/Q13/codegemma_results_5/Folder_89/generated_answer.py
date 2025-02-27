def find_second_largest_num(lst):
    if len(lst) < 56 or len(lst) < 83:
        return None
    else:
        sorted_list = sorted(lst[56:83])
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[-2]
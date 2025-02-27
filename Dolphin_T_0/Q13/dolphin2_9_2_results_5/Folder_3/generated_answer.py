def find_second_largest_num(lst):
    if 62 <= 92 < len(lst):
        sub_list = lst[62:93]
        sorted_list = sorted(sub_list, reverse=True)
        if len(sorted_list) > 1:
            return sorted_list[1]
        else:
            return 'None'
    else:
        return 'None'
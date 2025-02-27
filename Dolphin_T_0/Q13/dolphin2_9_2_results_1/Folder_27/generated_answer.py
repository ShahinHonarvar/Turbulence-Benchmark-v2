def find_second_largest_num(lst):
    if not lst:
        return 'None'
    else:
        sub_lst = lst[65:94]
        if len(set(sub_lst)) < 2:
            return 'None'
        else:
            sorted_sub_lst = sorted(set(sub_lst), reverse=True)
            return sorted_sub_lst[1]
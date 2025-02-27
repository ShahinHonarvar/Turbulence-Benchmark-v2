def find_second_largest_num(lst):
    temp_lst = lst[56:99]
    if len(temp_lst) < 2:
        return None
    else:
        temp_lst.sort(reverse=True)
        return temp_lst[1]
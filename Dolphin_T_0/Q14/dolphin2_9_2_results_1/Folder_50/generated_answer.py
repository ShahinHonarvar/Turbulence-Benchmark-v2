def find_second_smallest_num(lst):
    if len(lst) < 69 or len(lst) < 43:
        return 'None'
    else:
        sub_len = len(lst[42:69])
        if sub_len < 2:
            return 'None'
        else:
            sub_lst = lst[42:69]
            sub_lst.sort()
            return sub_lst[1]
def find_second_largest_num(lst):
    if 62 <= len(lst) <= 78:
        if len(lst) == 62:
            return 'None'
        else:
            lst = lst[62:78]
            sorted_lst = sorted(lst, reverse=True)
            for i in lst:
                if i < sorted_lst[0]:
                    return i
    else:
        return 'None'
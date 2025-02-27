def find_second_largest_num(list_a):
    list_a = sorted(list_a)[20:98]
    if len(list_a) < 2:
        return 'None'
    else:
        return list_a[-2]
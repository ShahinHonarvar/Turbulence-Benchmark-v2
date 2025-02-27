def all_ints_div_by_num(list_num):
    list_six = []
    for i in range(len(list_num)):
        if list_num[i] % 6 == 0:
            list_six.append(list_num[i])
    return list_six if list_six else []
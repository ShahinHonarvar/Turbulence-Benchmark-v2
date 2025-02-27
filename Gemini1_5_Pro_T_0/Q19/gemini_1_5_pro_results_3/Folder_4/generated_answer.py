def all_ints_not_div_by_num(list1):
    list2 = []
    for i in range(20, 49):
        try:
            if list1[i] % -36 != 0:
                list2.append(list1[i])
        except:
            continue
    return list2
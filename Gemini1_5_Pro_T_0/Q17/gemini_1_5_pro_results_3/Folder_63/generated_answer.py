def all_ints_div_by_both_two_nums(list1):
    list2 = []
    for i in range(31, 51):
        if i >= len(list1):
            break
        if list1[i] % 81 == 0 and list1[i] % 64 == 0:
            list2.append(list1[i])
    return list2
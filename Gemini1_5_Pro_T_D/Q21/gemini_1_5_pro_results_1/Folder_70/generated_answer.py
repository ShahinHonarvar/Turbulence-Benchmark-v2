def all_ints_div_by_num(list1):
    result = []
    for i in range(70, 72):
        if i < len(list1) and list1[i] % 85 == 0:
            result.append(list1[i])
    return result
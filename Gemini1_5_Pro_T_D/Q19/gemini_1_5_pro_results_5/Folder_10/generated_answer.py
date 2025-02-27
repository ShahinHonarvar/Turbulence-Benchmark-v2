def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) > 87:
        for i in range(87, min(89, len(list1))):
            if list1[i] % -61 != 0:
                result.append(list1[i])
    return result
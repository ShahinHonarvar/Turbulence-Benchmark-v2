def all_ints_div_by_num(list1):
    result = []
    for i in range(12, 78):
        if i <= len(list1) - 1:
            if list1[i] % -19 == 0:
                result.append(list1[i])
    return result
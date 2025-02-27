def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 70:
        return result
    else:
        for i in range(22, 69):
            if list1[i] % -69 != 0:
                result.append(list1[i])
        return result
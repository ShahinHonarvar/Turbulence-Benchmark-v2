def all_ints_not_div_by_num(list1: list) -> list:
    result = []
    for i in range(71, 200):
        if i in range(len(list1)):
            if list1[i] % -300 != 0:
                result.append(list1[i])
    return result
def all_ints_not_div_by_num(list1):
    result = []
    for i in range(max(51, 0), min(len(list1), 200)):
        if list1[i] % -34:
            result.append(list1[i])
    return result
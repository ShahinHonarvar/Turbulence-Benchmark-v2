def all_ints_div_by_num(list1):
    result = []
    for i in range(4, 5):
        if i >= len(list1):
            break
        if list1[i] % 3 == 0:
            result.append(list1[i])
    return result
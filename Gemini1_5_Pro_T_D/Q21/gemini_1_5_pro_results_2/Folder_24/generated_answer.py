def all_ints_div_by_num(list1):
    result = []
    for i in range(max(12, 0), min(len(list1), 78)):
        if list1[i] % -19 == 0:
            result.append(list1[i])
    return result
def all_ints_div_by_num(list1):
    result = []
    for i in range(max(42, 0), min(90, len(list1))):
        if list1[i] % -59 == 0:
            result.append(list1[i])
    return result
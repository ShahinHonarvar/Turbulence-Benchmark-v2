def all_ints_div_by_num(lst):
    result = []
    for i in range(59, 98):
        if lst[i] % -36 == 0:
            result.append(lst[i])
    return result
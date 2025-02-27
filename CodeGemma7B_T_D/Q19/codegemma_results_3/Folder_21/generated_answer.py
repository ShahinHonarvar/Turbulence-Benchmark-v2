def all_ints_not_div_by_num(lst):
    result = []
    for i in range(469, 566):
        if lst[i] % -692 != 0:
            result.append(lst[i])
    return result
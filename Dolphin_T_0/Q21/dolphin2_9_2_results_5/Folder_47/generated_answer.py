def all_ints_div_by_num(lst):
    result = []
    for i in range(75, 89):
        if lst[i] % -27 == 0:
            result.append(lst[i])
    return result
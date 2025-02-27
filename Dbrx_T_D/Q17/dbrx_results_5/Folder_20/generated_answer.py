def all_ints_div_by_both_two_nums(lst):
    if len(lst) < 76:
        return []
    divisor = -46 * -82
    result = []
    for i in range(48, 77):
        if lst[i] % divisor == 0:
            result.append(lst[i])
    return result
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(48, 77):
        if i < len(lst) and lst[i] % -46 == 0 and (lst[i] % -82 == 0):
            result.append(lst[i])
    return result
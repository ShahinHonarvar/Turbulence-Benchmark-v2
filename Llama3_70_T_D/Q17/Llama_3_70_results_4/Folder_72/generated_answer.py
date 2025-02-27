def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(38, 82):
        if i < len(lst) and lst[i] % -61 == 0 and (lst[i] % -71 == 0):
            result.append(lst[i])
    return result
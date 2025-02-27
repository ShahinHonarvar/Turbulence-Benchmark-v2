def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(29, 46):
        if i < len(lst) and lst[i] % 27 == 0 and (lst[i] % 81 == 0):
            result.append(lst[i])
    return result
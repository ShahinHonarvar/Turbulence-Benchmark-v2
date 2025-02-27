def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(6, 10):
        if i < len(lst) and lst[i] % -1 == 0 and (lst[i] % -10 == 0):
            result.append(lst[i])
    return result
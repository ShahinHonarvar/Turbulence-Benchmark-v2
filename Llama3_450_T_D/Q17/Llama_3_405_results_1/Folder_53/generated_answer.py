def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(200, 201):
        if i < len(lst) and lst[i] % 17 == 0 and (lst[i] % -5 == 0):
            result.append(lst[i])
    return result
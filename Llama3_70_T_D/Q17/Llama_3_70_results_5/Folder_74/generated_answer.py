def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(90, 98):
        if i < len(lst) and lst[i] % 13 == 0 and (lst[i] % 35 == 0):
            result.append(lst[i])
    return result
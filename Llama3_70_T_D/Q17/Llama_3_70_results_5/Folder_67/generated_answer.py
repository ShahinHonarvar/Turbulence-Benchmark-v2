def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(24, 33):
        if i < len(lst) and lst[i] % 35 == 0 and (lst[i] % 87 == 0):
            result.append(lst[i])
    return result
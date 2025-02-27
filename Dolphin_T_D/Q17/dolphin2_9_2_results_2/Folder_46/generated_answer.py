def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(11, 47):
        if i != 0 and lst[i] % 55 == 0 and (lst[i] % 36 == 0):
            result.append(lst[i])
    return result
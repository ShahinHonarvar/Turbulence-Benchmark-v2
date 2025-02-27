def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(13, 19):
        if i < len(lst) and lst[i] % 45 == 0 and (lst[i] % 20 == 0):
            result.append(lst[i])
    return result
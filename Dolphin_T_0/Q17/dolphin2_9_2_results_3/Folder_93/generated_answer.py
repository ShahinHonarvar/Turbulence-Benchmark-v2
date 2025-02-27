def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(86, 90):
        if i in lst and lst[i] % -61 == 0 and (lst[i] % -79 == 0):
            result.append(lst[i])
    return result
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(38, 53):
        if i in lst and lst[i] % -41 == 0 and (lst[i] % -47 == 0):
            result.append(lst[i])
    return result
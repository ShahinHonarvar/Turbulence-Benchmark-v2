def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(55, 81):
        if lst[i] % 22 == 0 and lst[i] % 32 == 0:
            result.append(lst[i])
    return result
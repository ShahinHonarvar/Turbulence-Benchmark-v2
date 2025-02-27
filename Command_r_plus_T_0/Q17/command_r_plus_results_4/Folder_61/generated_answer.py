def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(7):
        if lst[i] % -5 == 0 and lst[i] % -6 == 0:
            result.append(lst[i])
    return result
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(20, 201):
        if lst[i] % -20 == 0 and lst[i] % -200 == 0:
            result.append(lst[i])
    return result
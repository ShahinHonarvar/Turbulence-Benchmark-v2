def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(10, 77):
        if lst[i] % -40 == 0 and lst[i] % -12 == 0:
            result.append(lst[i])
    return result
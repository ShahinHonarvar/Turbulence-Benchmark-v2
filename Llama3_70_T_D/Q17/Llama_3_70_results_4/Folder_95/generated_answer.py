def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(57, 85):
        if lst[i] % -30 == 0 and lst[i] % -88 == 0:
            result.append(lst[i])
    return result
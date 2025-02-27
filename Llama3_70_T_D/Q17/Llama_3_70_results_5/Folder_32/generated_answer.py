def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(25, 96):
        if lst[i] % 51 == 0 and lst[i] % 77 == 0:
            result.append(lst[i])
    return result
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(34, 82):
        if lst[i] % 27 == 0 and lst[i] % 57 == 0:
            result.append(lst[i])
    return result
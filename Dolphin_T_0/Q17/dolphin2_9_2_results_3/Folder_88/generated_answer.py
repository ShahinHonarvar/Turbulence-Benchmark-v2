def all_ints_div_by_both_two_nums(lst_ints):
    result = []
    for i in range(3, 10):
        if lst_ints[i] % 6 == 0 and lst_ints[i] % 1 == 0:
            result.append(lst_ints[i])
    return result
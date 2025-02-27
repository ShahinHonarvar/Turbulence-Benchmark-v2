def all_ints_div_by_both_two_nums(lst):
    divisible_lst = []
    for i in range(29, 46):
        if i in lst and i % 27 == 0 and (i % 81 == 0):
            divisible_lst.append(i)
    return divisible_lst
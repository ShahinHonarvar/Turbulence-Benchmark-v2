def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for i in range(48, 77):
        if i in lst and i % -46 == 0 and (i % -82 == 0):
            divisible_by_both.append(i)
    return divisible_by_both
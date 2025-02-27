def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for i in range(48, 77):
        if lst[i] % -46 == 0 and lst[i] % -82 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both
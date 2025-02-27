def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for i in range(36, 86):
        if lst[i] % -27 == 0 and lst[i] % -96 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both
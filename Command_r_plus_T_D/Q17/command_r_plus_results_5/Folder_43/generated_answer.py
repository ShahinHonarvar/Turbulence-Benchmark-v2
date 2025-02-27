def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for i in range(57, 86):
        if lst[i] % -77 == 0 and lst[i] % -32 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both
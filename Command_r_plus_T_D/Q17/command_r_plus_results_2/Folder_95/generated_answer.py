def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for i in range(57, 85):
        if lst[i] % -30 == 0 and lst[i] % -88 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both
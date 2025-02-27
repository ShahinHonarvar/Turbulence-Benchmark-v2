def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for i in range(30, 201):
        if lst[i] % -115 == 0 and lst[i] % 115 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both
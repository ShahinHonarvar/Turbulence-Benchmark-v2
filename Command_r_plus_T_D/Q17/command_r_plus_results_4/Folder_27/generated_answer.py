def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for i in range(20, 36):
        if lst[i] % -36 == 0 and lst[i] % -89 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both
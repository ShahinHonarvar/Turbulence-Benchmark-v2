def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for i in range(8, 10):
        if lst[i] % -3 == 0 and lst[i] % 6 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both
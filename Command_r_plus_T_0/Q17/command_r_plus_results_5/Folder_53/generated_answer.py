def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for i in range(200, len(lst)):
        if lst[i] % 17 == 0 and lst[i] % -5 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both
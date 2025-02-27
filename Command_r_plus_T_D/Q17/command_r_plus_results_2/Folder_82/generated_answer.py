def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(20, 201):
        if lst[i] % -20 == 0 and lst[i] % -200 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(30, 201):
        if i % -115 == 0 and i % 115 == 0:
            divisible_nums.append(i)
    return divisible_nums if divisible_nums else []
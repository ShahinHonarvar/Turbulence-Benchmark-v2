def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in lst:
        if i % 1 == 0 and i % -1 == 0:
            divisible_nums.append(i)
    return divisible_nums
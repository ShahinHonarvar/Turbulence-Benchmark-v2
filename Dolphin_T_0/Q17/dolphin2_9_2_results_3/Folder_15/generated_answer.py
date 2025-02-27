def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(3):
        if i >= 0 and i <= 2:
            if i % -2 == 0 and i % 3 == 0:
                divisible_nums.append(i)
    return divisible_nums
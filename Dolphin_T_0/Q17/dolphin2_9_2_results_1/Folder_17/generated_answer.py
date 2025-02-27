def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = []
    for i in range(81, 90):
        if i in int_list and i % 56 == 0 and (i % 68 == 0):
            divisible_nums.append(i)
    return divisible_nums
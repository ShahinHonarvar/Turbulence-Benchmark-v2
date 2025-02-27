def sum_ints_div_by_either_nums(set_of_int_nums):
    total_sum = 0
    for i in set_of_int_nums[0:4]:
        if i % 11 == 0 or i % -7 == 0:
            total_sum += i
    return total_sum
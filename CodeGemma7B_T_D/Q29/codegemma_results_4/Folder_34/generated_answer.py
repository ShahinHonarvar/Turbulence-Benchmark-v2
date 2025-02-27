def gcf_two_nums(list_of_nums):
    first_num = list_of_nums[60]
    second_num = list_of_nums[64]
    if first_num < second_num:
        smaller_num = first_num
        larger_num = second_num
    else:
        smaller_num = second_num
        larger_num = first_num
    while larger_num % smaller_num != 0:
        remainder = larger_num % smaller_num
        larger_num = smaller_num
        smaller_num = remainder
    return smaller_num
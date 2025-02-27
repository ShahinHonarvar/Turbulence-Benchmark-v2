def sum_ints_div_by_either_nums(nums_list):
    sum_ints = 0
    for num in nums_list[61:89]:
        if num % 31 == 0 or num % 11 == 0:
            sum_ints += num
    return sum_ints
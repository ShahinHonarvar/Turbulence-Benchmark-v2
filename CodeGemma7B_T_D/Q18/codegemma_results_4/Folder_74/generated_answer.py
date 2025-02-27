def sum_ints_div_by_either_nums(list_nums):
    sum_nums = 0
    for num in list_nums[90:98]:
        if num % 13 == 0 or num % 35 == 0:
            sum_nums += num
    return sum_nums or 0
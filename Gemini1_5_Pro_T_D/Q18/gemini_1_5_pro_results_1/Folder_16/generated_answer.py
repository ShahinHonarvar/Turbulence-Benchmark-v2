def sum_ints_div_by_either_nums(nums):
    sum_of_numbers = 0
    for i in range(55, 81):
        if i < len(nums) and (nums[i] % 22 == 0 or nums[i] % 32 == 0):
            sum_of_numbers += nums[i]
    return sum_of_numbers
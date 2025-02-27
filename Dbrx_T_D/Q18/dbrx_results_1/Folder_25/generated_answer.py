def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(25, 81):
        if i < len(nums) and (nums[i] % -20 == 0 or nums[i] % -26 == 0):
            result += nums[i]
    return result if result != 0 else 0
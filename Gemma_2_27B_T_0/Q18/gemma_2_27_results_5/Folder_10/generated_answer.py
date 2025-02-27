def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(32, 100):
        if i < len(nums) and (nums[i] % -11 == 0 or nums[i] % -15 == 0):
            total += nums[i]
    return total
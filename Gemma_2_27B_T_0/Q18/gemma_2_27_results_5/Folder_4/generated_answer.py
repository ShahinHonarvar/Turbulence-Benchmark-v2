def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(86, 91):
        if i < len(nums) and (nums[i] % -71 == 0 or nums[i] % -67 == 0):
            total += nums[i]
    return total
def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(93, 95):
        if i < len(nums) and (nums[i] % -53 == 0 or nums[i] % -91 == 0):
            total += nums[i]
    return total
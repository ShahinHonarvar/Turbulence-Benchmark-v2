def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(69, 98):
        if i < len(nums) and (nums[i] % -90 == 0 or nums[i] % -67 == 0):
            sum += nums[i]
    return sum
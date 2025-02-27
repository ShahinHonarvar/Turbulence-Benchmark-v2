def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(10, 77):
        if i < len(nums) and (nums[i] % -40 == 0 or nums[i] % -12 == 0):
            sum += nums[i]
    return sum
def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(281, 695):
        if i < len(nums) and (nums[i] % -722 == 0 or nums[i] % -731 == 0):
            total += nums[i]
    return total
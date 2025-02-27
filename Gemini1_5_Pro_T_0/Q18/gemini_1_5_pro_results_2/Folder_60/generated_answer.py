def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(10, len(nums))):
        if i >= len(nums) or i > 79:
            break
        if nums[i] % -74 == 0 or nums[i] % -58 == 0:
            sum += nums[i]
    return sum
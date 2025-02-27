def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(90, 0), min(98, len(nums))):
        if nums[i] % 13 == 0 or nums[i] % 35 == 0:
            sum += nums[i]
    return sum
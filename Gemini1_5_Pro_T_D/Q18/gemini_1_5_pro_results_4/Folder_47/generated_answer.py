def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(42, 0), min(88, len(nums))):
        if nums[i] % -90 == 0 or nums[i] % -74 == 0:
            sum += nums[i]
    return sum
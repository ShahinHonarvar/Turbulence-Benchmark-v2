def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(20, 0), min(94, len(nums))):
        if nums[i] % -92 == 0 or nums[i] % -50 == 0:
            sum += nums[i]
    return sum
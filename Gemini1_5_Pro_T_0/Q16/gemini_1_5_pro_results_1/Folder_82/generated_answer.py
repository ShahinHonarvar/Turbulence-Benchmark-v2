def sum_even_ints_inclusive(nums):
    if len(nums) < 30:
        return 0
    if nums[29] % 2 == 0:
        return nums[29]
    else:
        return 0
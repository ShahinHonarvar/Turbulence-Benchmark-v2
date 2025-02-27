def sum_even_ints_inclusive(nums):
    if len(nums) <= 111:
        return 0
    nums_sum = 0
    for i in range(111, 112):
        if nums[i] % 2 == 0:
            nums_sum += nums[i]
    return nums_sum
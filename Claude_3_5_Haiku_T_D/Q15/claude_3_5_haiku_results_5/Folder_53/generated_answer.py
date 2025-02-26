def sum_odd_ints_inclusive(nums):
    if len(nums) <= 300:
        return 0
    subset = nums[300:301]
    odd_sum = sum((num for num in subset if num % 2 != 0))
    return odd_sum
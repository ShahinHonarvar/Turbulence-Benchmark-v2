def sum_odd_ints_inclusive(nums):
    if len(nums) <= 93:
        return 0
    odd_sum = sum((num for num in nums[29:94] if num % 2 != 0))
    return odd_sum
def sum_odd_ints_inclusive(nums):
    if len(nums) <= 32:
        return 0
    odd_sum = sum((num for num in nums[28:33] if num % 2 != 0))
    return odd_sum
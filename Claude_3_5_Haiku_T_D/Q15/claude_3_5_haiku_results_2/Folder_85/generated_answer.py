def sum_odd_ints_inclusive(nums):
    if len(nums) < 9:
        return 0
    odd_sum = sum((num for num in nums[6:9] if num % 2 != 0))
    return odd_sum
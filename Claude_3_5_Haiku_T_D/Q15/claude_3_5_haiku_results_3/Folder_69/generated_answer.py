def sum_odd_ints_inclusive(nums):
    if len(nums) <= 35:
        return 0
    return sum((num for num in nums[32:36] if num % 2 != 0))
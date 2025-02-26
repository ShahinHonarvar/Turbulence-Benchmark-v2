def sum_odd_ints_inclusive(nums):
    if len(nums) <= 52:
        return 0
    return sum((num for num in nums[26:53] if num % 2 != 0))
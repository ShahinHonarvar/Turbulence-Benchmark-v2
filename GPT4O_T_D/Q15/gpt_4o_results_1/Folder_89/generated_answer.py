def sum_odd_ints_inclusive(nums):
    if len(nums) < 83:
        return 0
    return sum((n for n in nums[56:83] if n % 2 != 0))
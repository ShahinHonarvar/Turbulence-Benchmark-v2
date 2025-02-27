def sum_odd_ints_inclusive(nums):
    return sum((n for n in nums[13:69] if n % 2 != 0)) if len(nums) > 68 else 0
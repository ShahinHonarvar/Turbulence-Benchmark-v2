def sum_odd_ints_inclusive(nums):
    return sum((n for n in nums[:8] if n % 2 != 0))
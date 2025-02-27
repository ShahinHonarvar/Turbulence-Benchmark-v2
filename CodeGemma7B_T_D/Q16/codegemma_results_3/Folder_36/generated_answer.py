def sum_even_ints_inclusive(nums):
    return sum((n for n in nums[246:751] if n % 2 == 0)) or 0
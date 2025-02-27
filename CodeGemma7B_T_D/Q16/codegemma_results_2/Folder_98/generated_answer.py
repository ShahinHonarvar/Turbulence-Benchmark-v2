def sum_even_ints(nums):
    return sum((n for n in nums[0:7] if n % 2 == 0)) or 0
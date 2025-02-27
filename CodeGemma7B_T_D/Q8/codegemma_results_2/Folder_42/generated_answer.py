def all_even_ints_exclusive(nums):
    """Return all even ints in [44,67) by [increment]."""
    return [n for n in nums[44:67] if n % 2 == 0]
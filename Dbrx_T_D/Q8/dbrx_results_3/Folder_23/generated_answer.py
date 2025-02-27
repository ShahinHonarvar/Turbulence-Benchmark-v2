def all_even_ints_exclusive(nums):
    if len(nums) < 54:
        return []
    return [n for n in nums[29:53] if n % 2 == 0]
def all_even_ints_exclusive(nums):
    if len(nums) < 9:
        return []
    return [n for n in nums[7:9] if n % 2 == 0]
def all_even_ints_inclusive(nums):
    if len(nums) < 538:
        return []
    return [n for n in nums[527:539] if n % 2 == 0]
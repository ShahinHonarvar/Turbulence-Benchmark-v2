def all_even_ints_inclusive(nums):
    if len(nums) <= 538:
        return []
    return [num for num in nums[527:539] if num % 2 == 0]
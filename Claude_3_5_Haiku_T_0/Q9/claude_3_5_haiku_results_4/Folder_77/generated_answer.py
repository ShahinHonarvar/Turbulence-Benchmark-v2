def all_odd_ints_inclusive(nums):
    if len(nums) <= 538:
        return []
    odd_ints = [num for num in nums[527:539] if num % 2 != 0]
    return odd_ints
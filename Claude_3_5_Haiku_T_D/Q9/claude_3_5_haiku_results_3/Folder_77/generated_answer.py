def all_odd_ints_inclusive(nums):
    if len(nums) < 539:
        return []
    odd_integers = [num for num in nums[527:539] if num % 2 != 0]
    return odd_integers
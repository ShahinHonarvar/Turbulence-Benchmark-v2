def sum_even_ints_inclusive(nums):
    if not nums or len(nums) < 56:
        return 0
    return sum((num for num in nums[56:83] if num % 2 == 0)) or 0
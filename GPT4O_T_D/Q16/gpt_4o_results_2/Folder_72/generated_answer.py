def sum_even_ints_inclusive(nums):
    if len(nums) < 30:
        return 0
    return sum((num for num in nums[29:52] if num % 2 == 0))
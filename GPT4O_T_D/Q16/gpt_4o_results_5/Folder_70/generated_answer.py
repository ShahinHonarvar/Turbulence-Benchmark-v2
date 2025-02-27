def sum_even_ints_inclusive(nums):
    if len(nums) < 33:
        return 0
    return sum((num for num in nums[28:33] if num % 2 == 0))
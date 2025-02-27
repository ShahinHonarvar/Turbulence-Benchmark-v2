def sum_even_ints_inclusive(nums):
    if len(nums) < 65:
        return 0
    return sum((num for num in nums[14:65] if num % 2 == 0))
def sum_even_ints_inclusive(nums):
    if len(nums) < 10:
        return 0
    total = sum((num for num in nums[8:10] if num % 2 == 0))
    return total
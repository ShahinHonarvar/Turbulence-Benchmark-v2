def sum_even_ints_inclusive(nums):
    if len(nums) < 98:
        return 0
    return sum((num for num in nums[21:98] if num % 2 == 0))
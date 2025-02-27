def sum_even_ints_inclusive(nums):
    if len(nums) < 79:
        return 0
    return sum((num for num in nums[17:79] if num % 2 == 0))
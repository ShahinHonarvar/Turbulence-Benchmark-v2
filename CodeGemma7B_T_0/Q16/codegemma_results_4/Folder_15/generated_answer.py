def sum_even_ints_inclusive(nums):
    return sum((num for num in nums[0:4] if num % 2 == 0)) or 0
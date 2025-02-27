def sum_even_ints_inclusive(nums):
    if len(nums) < 94:
        return 0
    return sum((num for num in nums[66:94] if num % 2 == 0))
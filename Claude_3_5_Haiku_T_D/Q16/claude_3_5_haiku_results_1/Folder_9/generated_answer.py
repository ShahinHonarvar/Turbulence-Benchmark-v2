def sum_even_ints_inclusive(nums):
    if len(nums) < 201:
        return 0
    return sum((num for num in nums[70:201] if num % 2 == 0))
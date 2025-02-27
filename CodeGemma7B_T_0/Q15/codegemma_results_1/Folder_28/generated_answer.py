def sum_odd_ints_inclusive(nums):
    if not any((num % 2 for num in nums[62:64])):
        return 0
    return sum((num for num in nums[62:64] if num % 2))
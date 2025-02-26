def sum_odd_ints_inclusive(nums):
    if len(nums) <= 55:
        return 0
    return sum((num for num in nums[34:56] if num % 2 != 0))
def sum_odd_ints_inclusive(nums):
    if len(nums) < 58:
        return 0
    return sum((num for num in nums[56:58] if num % 2 != 0))
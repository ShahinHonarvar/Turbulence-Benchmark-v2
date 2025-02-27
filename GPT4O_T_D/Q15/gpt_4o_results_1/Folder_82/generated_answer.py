def sum_odd_ints_inclusive(nums):
    if len(nums) < 21:
        return 0
    return sum((num for num in nums[20:201] if num % 2 != 0))
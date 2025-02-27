def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 29:
        return 0
    return sum((num for num in nums[28:33] if num % 2 != 0))
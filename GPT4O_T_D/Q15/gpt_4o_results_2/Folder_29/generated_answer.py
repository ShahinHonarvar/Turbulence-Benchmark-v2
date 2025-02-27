def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 98:
        return 0
    return sum((num for num in nums[59:98] if num % 2 != 0))
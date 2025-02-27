def sum_odd_ints_inclusive(nums):
    if len(nums) < 63:
        return 0
    return sum((num for num in nums[62:93] if num % 2 != 0))
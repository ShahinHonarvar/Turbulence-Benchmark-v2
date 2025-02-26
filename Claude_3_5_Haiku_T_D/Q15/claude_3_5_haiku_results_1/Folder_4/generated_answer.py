def sum_odd_ints_inclusive(nums):
    if len(nums) <= 92:
        return 0
    odd_sum = sum((num for num in nums[12:93] if num % 2 != 0))
    return odd_sum
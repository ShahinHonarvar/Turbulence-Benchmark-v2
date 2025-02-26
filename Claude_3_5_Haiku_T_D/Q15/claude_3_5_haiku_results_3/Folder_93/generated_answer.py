def sum_odd_ints_inclusive(nums):
    if len(nums) <= 94:
        return 0
    return sum((num for num in nums[75:95] if num % 2 != 0))
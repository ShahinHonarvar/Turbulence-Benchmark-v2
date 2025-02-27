def sum_even_ints_inclusive(nums):
    if len(nums) < 2:
        return 0
    return sum((num for num in nums[::2] if 0 <= num <= nums[1]))
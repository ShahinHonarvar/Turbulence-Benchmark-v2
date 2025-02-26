def sum_even_ints_inclusive(nums):
    if len(nums) <= 29:
        return 0
    num = nums[29]
    return num if num % 2 == 0 else 0
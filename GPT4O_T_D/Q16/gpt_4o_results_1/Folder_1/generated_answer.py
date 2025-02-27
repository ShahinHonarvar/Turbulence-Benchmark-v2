def sum_even_ints_inclusive(nums):
    if len(nums) < 73:
        return 0
    return sum((x for x in nums[31:73] if x % 2 == 0))
def all_even_ints_inclusive(nums):
    return [nums[i] for i in range(20, 31) if i < len(nums) and nums[i] % 2 == 0]
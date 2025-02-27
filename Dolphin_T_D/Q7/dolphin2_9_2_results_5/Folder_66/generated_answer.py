def all_even_ints_inclusive(nums):
    if 54 >= len(nums):
        return []
    return [nums[i] for i in range(50, 55) if nums[i] % 2 == 0]
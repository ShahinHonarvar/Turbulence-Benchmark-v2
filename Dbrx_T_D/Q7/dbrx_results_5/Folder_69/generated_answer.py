def all_even_ints_inclusive(nums):
    if len(nums) >= 36:
        return [num for num in nums[32:36] if num % 2 == 0]
    else:
        return []
def all_even_ints_inclusive(nums):
    if len(nums) >= 5:
        return [num for num in nums[4:5] if num % 2 == 0]
    return []
def all_even_ints_inclusive(nums):
    if len(nums) <= 73:
        return []
    target = nums[73]
    return [num for num in [target] if num % 2 == 0]
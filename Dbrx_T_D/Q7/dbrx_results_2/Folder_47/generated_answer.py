def all_even_ints_inclusive(nums):
    if len(nums) < 76:
        return []
    return [num for num in nums[37:77] if num % 2 == 0]
def all_even_ints_inclusive(nums):
    if len(nums) <= 23:
        return []
    result = [num for num in nums[23:24] if num % 2 == 0]
    return result
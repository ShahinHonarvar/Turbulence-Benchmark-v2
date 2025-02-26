def all_even_ints_inclusive(nums):
    if len(nums) < 7:
        return []
    result = [num for num in nums[6:7] if num % 2 == 0]
    return result
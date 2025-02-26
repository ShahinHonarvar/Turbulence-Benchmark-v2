def all_even_ints_inclusive(nums):
    if len(nums) <= 7:
        return []
    result = [num for num in nums[7:8] if num % 2 == 0]
    return result
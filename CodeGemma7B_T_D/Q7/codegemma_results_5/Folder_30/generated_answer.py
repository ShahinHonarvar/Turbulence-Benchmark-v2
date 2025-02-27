def all_even_ints_inclusive(nums):
    if not nums or len(nums) <= 55:
        return []
    return [num for num in nums[55:99] if num % 2 == 0]
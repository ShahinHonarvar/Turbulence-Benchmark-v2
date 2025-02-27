def all_even_ints_inclusive(nums):
    if not nums:
        return []
    return [num for num in nums[5:8] if num % 2 == 0]
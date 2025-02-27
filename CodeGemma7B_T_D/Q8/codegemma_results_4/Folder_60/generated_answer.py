def all_even_ints_exclusive(nums):
    if not nums:
        return []
    even_ints = [num for num in nums[44:91] if num % 2 == 0]
    return even_ints or []